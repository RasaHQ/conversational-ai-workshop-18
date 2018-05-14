from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

from core_extensions.policy_trainer import CustomAgent
from rasa_core.featurizers import (LabelTokenizerSingleStateFeaturizer,
                                   FullDialogueTrackerFeaturizer,
                                   MaxHistoryTrackerFeaturizer)
from rasa_core.policies.embedding_policy import EmbeddingPolicy
from rasa_core.policies.keras_policy import KerasPolicy

logger = logging.getLogger(__name__)


def train_domain_policy(story_filename,
                        output_path=None,
                        exclusion_file=None,
                        exclusion_percentage=None,
                        starspace=True,
                        epoch_no=2000,
                        embed_dim=10):
    """Trains a new deterministic domain policy using the stories
    (json format) in `story_filename`."""
    if starspace:
        featurizer = FullDialogueTrackerFeaturizer(
                        LabelTokenizerSingleStateFeaturizer())
        policies = [EmbeddingPolicy(featurizer)]
        epochs = epoch_no
    else:
        featurizer = MaxHistoryTrackerFeaturizer(
                        LabelTokenizerSingleStateFeaturizer(),
                        max_history=20)
        policies = [KerasPolicy(featurizer)]
        epochs = 400

    agent = CustomAgent("bAbI_domain.yml",
                        policies=policies)
    data = agent.load_data(story_filename,
                           remove_duplicates=True,
                           augmentation_factor=0,
                           exclusion_file=exclusion_file,
                           exclusion_percentage=exclusion_percentage)

    agent.train(data,
                rnn_size=32,
                epochs=epochs,
                embed_dim=embed_dim,
                use_attention=True)

    agent.persist(model_path=output_path)


if __name__ == '__main__':
    logging.basicConfig(level="DEBUG")
    train_domain_policy(story_filename="data_bAbI/train/",
                        output_path='models/dialogue_embed',
                        # exclusion_file='data/train/hotel_chitchat.md',
                        # exclusion_percentage=100,
                        embed_dim=20
                        )
    logger.info("Finished training domain policy.")
