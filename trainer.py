from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

from rasa_extensions.core.full_agent import FullAgent
from rasa_extensions.core.babi_starspace_policy import bAbIStarspacePolicy
from rasa_extensions.core.label_featurizer import LabelFeaturizer

logger = logging.getLogger(__name__)


def train_domain_policy(story_filename, output_path=None):
    """Trains a new deterministic domain policy using the stories
    (json format) in `story_filename`."""

    policies = [bAbIStarspacePolicy()]
    featurizer = LabelFeaturizer()

    agent = FullAgent("domain.yml",
                      featurizer=featurizer,
                      policies=policies)

    agent.train(story_filename,
                remove_duplicates=True,
                epochs=200,
                model_path=output_path,
                augmentation_factor=0)


if __name__ == '__main__':
    logging.basicConfig(level="DEBUG")
    train_domain_policy(story_filename="data/train/",
                        output_path='models/dialogue')
    logger.info("Finished training domain policy.")
