from dataclasses import dataclass

from typing import Optional

import torch
from transformers.modeling_outputs import ModelOutput


@dataclass
class ClipOutputFeatures(ModelOutput):
    """
    Data class of features from AlbefFeatureExtractor.

    Args:
        image_embeds: `torch.FloatTensor` of shape `(batch_size, 1, embed_dim)`, `optional`
        image_features: `torch.FloatTensor` of shape `(batch_size, 1, feature_dim)`, `optional`
        text_embeds: `torch.FloatTensor` of shape `(batch_size, 1, embed_dim)`, `optional`
        text_features: `torch.FloatTensor` of shape `(batch_size, 1, feature_dim)`, `optional`
    """

    image_embeds: Optional[torch.FloatTensor] = None
    image_features: Optional[torch.FloatTensor] = None

    text_embeds: Optional[torch.FloatTensor] = None
    text_features: Optional[torch.FloatTensor] = None


@dataclass
class ClipOutput(ModelOutput):
    intermediate_output: Optional[ClipOutputFeatures] = None

    logit_scale_exp: Optional[torch.FloatTensor] = None

    loss: Optional[torch.FloatTensor] = None