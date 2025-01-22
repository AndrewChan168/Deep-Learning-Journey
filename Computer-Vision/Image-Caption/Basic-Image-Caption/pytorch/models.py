import torch
import torch.nn as nn
import torchvision.models as models
import torchvision.transforms as transforms
from torch.nn.utils.rnn import pack_padded_sequence


class CNNEncoder(nn.Module):
    def __init__(self, embedding_size):
        super(CNNEncoder, self).__init__()
        resnet = models.resnet50(weights=True)
        layers = list(resnet.children())[:-1] # remove last full connected layer
        self.resnet_base = nn.Sequential(*layers)
        self.fc = nn.Linear(resnet.fc.in_features, embedding_size)
        self.batch_norm = nn.BatchNorm1d(embedding_size, momentum=0.01)

    def forward(self, img):
        """Extract feature vectors from input images."""
        with torch.no_grad():
            features = self.resnet_base(img)
        features = features.reshape(features.size(0), -1)
        final_features = self.batch_norm(self.fc(features))
        return final_features


class RNNModel(nn.Module):
    def __init__(self, embedding_size, hidden_layer_size, vocabulary_size, num_layers, max_seq_len=20):
        super(RNNModel, self).__init__()
        self.embedding_layer = nn.Embedding(vocabulary_size, embedding_size)
        self.lstm_layer = nn.LSTM(embedding_size, hidden_layer_size, num_layers, batch_first=True)
        self.linear_layer = nn.Linear(hidden_layer_size, vocabulary_size)
        self.max_seq_len = max_seq_len

    def forward(self, input_embeds, captions, lengths):
        """Decode image feature vectors and generates captions."""
        embeds = self.embedding_layer(captions)
        embeds = torch.cat((input_embeds.unsqueeze(1), embeds), 1)
        rnn_inputs = pack_padded_sequence(embeds, lengths, batch_first=True) 
        hidden_outputs, _ = self.lstm_layer(rnn_inputs)
        outputs = self.linear_layer(hidden_outputs)
        return outputs

    def sample(self, input_embeds, rnn_states=None):
        """Generate captions for given image features using greedy search."""
        token_idxs = []
        rnn_inputs = input_embeds.unsqueeze(1)
        for idx in range(self.max_seq_len):
            hidden_outputs, rnn_states = self.lstm_layer(rnn_inputs, rnn_states) # hidden: (batch_size, 1, hidden_size)
            outputs = self.linear_layer(hidden_outputs.squeeze(1))
            _, predictions = outputs.max(1)
            token_idxs.append(predictions)
            rnn_inputs = (self.embedding_layer(predictions)).unsqueeze(1)
        return torch.stack(token_idxs, 1)


def collate_function(batch):
    """Creates mini-batch tensors from the list of tuples (image, caption).

    we build our own custom collate_fn because  merging caption (including padding) 
    is not supported in default collate_fn
    Args:
        batch: list of tuple (image, caption).
                - image: torch tensor of shape (3, 256, 256).
                - caption: torch tensor of shape (?); variable length.
    Returns:
        images: torch tensor of shape (batch_size, 3, 256, 256).
        targets: torch tensor of shape (batch_size, padded_length).
        lengths: list; valid length for each padded caption.
    """
    # Sort a data list by caption length (descending order).
    batch.sort(key=lambda d: len(d[1]), reverse=True)
    imgs, caps = zip(*batch)

    # Merge images (from list of 3D tensors to 4D tensor).
    # Originally, imgs is a list of <batch_size> number of RGB images with dimensions (3, 256, 256)
    # This line of code turns it into a single tensor of dimensions (<batch_size>, 3, 256, 256)
    imgs = torch.stack(imgs, 0)

    # Merge captions (from list of 1D tensors to 2D tensor), similar to merging of images donw above.
    cap_lens = [len(cap) for cap in caps]
    targets = torch.zeros(len(caps), max(cap_lens)).long()
    for i, cap in enumerate(caps):
        end = cap_lens[i]
        targets[i, :end] = cap[:end]        
    return imgs, targets, cap_lens