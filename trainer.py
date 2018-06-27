from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

from core_extensions.policy_trainer import CustomAgent
from rasa_core.featurizers import (LabelTokenizerSingleStateFeaturizer,
                                   FullDialogueTrackerFeaturizer,
                                   MaxHistoryTrackerFeaturizer,
                                   BinarySingleStateFeaturizer)
from rasa_core.policies.embedding_policy import EmbeddingPolicy
from rasa_core.policies.keras_policy import KerasPolicy

logger = logging.getLogger(__name__)


def train_domain_policy(story_filename,
                        output_path=None,
                        exclusion_file=None,
                        exclusion_percentage=None,
                        starspace=True,
                        split_symbol='_',
                        epoch_no=2000,
                        embed_dim=20,
                        attn_shift_range=5,
                        attn_before_rnn=True,
                        attn_after_rnn=True,
                        calc_acc_ones_in_epochs=20,
                        binary_feat=False):
    """Trains a new deterministic domain policy using the stories
    (json format) in `story_filename`."""
    if starspace:
        featurizer = FullDialogueTrackerFeaturizer(
                        LabelTokenizerSingleStateFeaturizer(split_symbol=split_symbol))
                        # BinarySingleStateFeaturizer())
        policies = [EmbeddingPolicy(featurizer)]
        epochs = epoch_no
        batch_size=[8,32]
    elif binary_feat:
        featurizer = MaxHistoryTrackerFeaturizer(
                        BinarySingleStateFeaturizer(),
                        max_history=38)
        policies = [KerasPolicy(featurizer)]
        epochs = 200
        batch_size=32
    else:
        featurizer = MaxHistoryTrackerFeaturizer(
                        LabelTokenizerSingleStateFeaturizer(),
                        max_history=38)
        policies = [KerasPolicy(featurizer)]
        epochs = 200
        batch_size=32

    agent = CustomAgent("domain.yml",
                        policies=policies)
    data = agent.load_data(story_filename,
                           remove_duplicates=True,
                           augmentation_factor=0,
                           exclusion_file=exclusion_file,
                           exclusion_percentage=exclusion_percentage)

    agent.train(data,
                rnn_size=64,
                epochs=epochs,
                embed_dim=embed_dim,
                sparse_attention=False,
                attn_shift_range=attn_shift_range,
                attn_before_rnn=attn_before_rnn,
                attn_after_rnn=attn_after_rnn,
                batch_size=batch_size,
                calc_acc_ones_in_epochs=calc_acc_ones_in_epochs)

    agent.persist(model_path=output_path)


if __name__ == '__main__':
    logging.basicConfig(level="DEBUG")
    train_domain_policy(story_filename="data-simulated/train/",
                        output_path='models/dialogue_embed',
                        exclusion_file='data-simulated/train/simulated_hotel_train.md',
                        exclusion_percentage=0,
                        embed_dim=20,
                        epoch_no=2000,
                        attn_before_rnn=True,
                        attn_after_rnn=True,
                        )
    logger.info("Finished training domain policy.")
