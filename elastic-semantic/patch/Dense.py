import torch
from torch import Tensor
from torch import nn
from torch import functional as F
from typing import Union, Tuple, List, Iterable, Dict
import os
import json
from ..util import fullname, import_from_string


class Dense(nn.Module):
    """Feed-forward function with  activiation function.

    This layer takes a fixed-sized sentence embedding and passes it through a feed-forward layer. Can be used to generate deep averaging networs (DAN).
    """
    def __init__(self, in_features, out_features, bias=True, activation_function=nn.Tanh()):
        super(Dense, self).__init__()
        self.in_features = in_features
        self.out_features = out_features
        self.bias = bias
        self.activation_function = activation_function
        self.linear = nn.Linear(in_features, out_features, bias=bias)

    def forward(self, features: Dict[str, Tensor]):
        features.update({'sentence_embedding': self.activation_function(self.linear(features['sentence_embedding']))})
        return features

    def get_sentence_embedding_dimension(self) -> int:
        return self.out_features

    def save(self, output_path):
        with open(os.path.join(output_path, 'config.json'), 'w') as fOut:
            json.dump({'in_features': self.in_features, 'out_features': self.out_features, 'bias': self.bias, 'activation_function': fullname(self.activation_function)}, fOut)

        torch.save(self.state_dict(), os.path.join(output_path, 'pytorch_model.bin'))

    @staticmethod
    def load(input_path, map_location=torch.device('cpu')):
        with open(os.path.join(input_path, 'config.json')) as fIn:
            config = json.load(fIn)

        config['activation_function'] = import_from_string(config['activation_function'])()
        model = Dense(**config)
        model.load_state_dict(torch.load(os.path.join(input_path, 'pytorch_model.bin'), map_location=map_location))
        return model
