from torch import nn

class NextTokenLSTM(nn.Module):
    def __init__(self, vocab_size, input_size=128, n_embed=128, n_layers=3, drop_prob=0.2):
        super().__init__()
        self.vocab_size = vocab_size
        self.input_size = input_size
        self.n_embed = n_embed
        self.n_layers = n_layers
        self.drop_prob = drop_prob
        self.embedding = nn.Embedding(self.vocab_size, self.n_embed)
        self.lstm = nn.LSTM(input_size=self.input_size, hidden_size=self.n_embed, num_layers=self.n_layers, dropout=self.drop_prob, batch_first=True)
        self.full_connected = nn.Linear(self.input_size, self.vocab_size)

    def forward(self, x, hc):
        embed = self.embedding(x)
        o, hc = self.lstm(embed, hc)
        y = self.full_connected(o)
        return y, hc

    def initalize_hidden(self, batch_size):
        weight = next(self.parameters()).data
        return (weight.new(self.n_layers, batch_size, self.n_embed).zero_(), weight.new(self.n_layers, batch_size, self.n_embed).zero_())