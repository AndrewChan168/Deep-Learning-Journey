import nltk
import torch
from collections import Counter 
from pycocotools.coco import COCO
import torch.nn as nn
import torch.utils.data as data
import torchvision.models as models
import torchvision.transforms as transforms

def build_tokens_counter(json_path):
    coco = COCO(json_path)
    counter = Counter()
    ids = coco.anns.keys()
    for i, id_ in enumerate(ids):
        caption = str(coco.anns[id_]['caption'])
        tokens = nltk.tokenize.word_tokenize(caption.lower())
        counter.update(tokens)
        if (i+1)%10000 == 0:
            print("[{}/{}] Tokenized the captions.".format(i+1, len(ids)))
    return counter


class TokenIndex:
    def __init__(self):
        self.token2Idx = {}
        self.idx2Token = {}
        self.current_idx = 0

    def __call__(self, token):
        if token in self.token2Idx:
            return self.token2Idx[token]
        else:
            return self.token2Idx['<unk>']
            
    def __len__(self):
        return len(self.token2Idx)
    
    def add_token(self, token):
        if not token in self.token2Idx:
            self.token2Idx[token] = self.current_idx
            self.idx2Token[self.current_idx] = token
            self.current_idx += 1


def build_tokenIndex(tokens_counter, threshold):
    kept_tokens = [t for t,c in tokens_counter.items() if c>=threshold]
    tokenIndex = TokenIndex()
    tokenIndex.add_token('<pad>')
    tokenIndex.add_token('<unk>')
    tokenIndex.add_token('<start>')
    tokenIndex.add_token('<end>')
    for t in kept_tokens:
        tokenIndex.add_token(t)
    return tokenIndex


def reshape_image(image, shape_tuple):
    return image.resize(shape_tuple, Image.LANCZOS)


def reshape_images_from_folder(folder_path, output_path, shape_tuple):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    image_paths = os.listdir(folder_path)
    for i, img_path in enumerate(image_paths):
        with open(os.path.join(folder_path, img_path), 'rb') as file:
            with Image.open(file) as img:
                img_reshaped = reshape_image(img, shape_tuple)
                img_reshaped.save(os.path.join(output_path, img_path), img_reshaped.format)
        if (i+1) % 2000 == 0:
            print ("[{}/{}] Resized the images and saved into '{}'.".format(i+1, len(image_paths), output_path))


class CustomCocoDataset(data.Dataset):
    """COCO Custom Dataset compatible with torch.utils.data.DataLoader."""
    def __init__(self, image_path, coco_json_path, token2Index, transform_pl=None):
        """
        Args:
            image_path: image directory
            coco_json_path: coco annotation file path.
            tokenIndex: tokenIndex object
            transform_pl: pytorch transformation pipeline for image
        """
        self.image_root_dir = image_path
        self.coco_data = COCO(coco_json_path)
        self.indices = list(self.coco_data.anns.keys())
        self.token2Index = token2Index
        self.transform_pl = transform_pl

    def __getitem__(self, idx):
        """return data in pair (image & caption)"""
        anno_id = self.indices[idx]
        caption = self.coco_data.anns[anno_id]['caption']
        img_id = self.coco_data.anns[anno_id]['image_id']
        img_nme = self.coco_data.loadImgs(img_id)[0]['file_name']
        img = Image.open(os.path.join(self.image_root_dir, img_nme)).convert('RGB')
        if self.transform_pl is not None:
            img = self.transform_pl(img)

        # Convert caption (string) to word ids
        word_tokens = nltk.tokenize.word_tokenize(str(caption).lower())
        caption = []
        caption.append(self.token2Index('<start>'))
        caption.extend([self.token2Index(token) for token in word_tokens])
        caption.append(self.token2Index('<end>'))
        ground_truth = torch.Tensor(caption)
        return img, ground_truth

    def __len__(self):
        return len(self.indices)