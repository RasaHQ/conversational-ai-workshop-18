# generalisation-example
This is the bot we used for the experiments in our paper on "Few-shot
Generalisation Across Dialogue Tasks".

## Installation
To install all the requirements needed to use this bot, please run:
```
pip install -r requirements.txt
```

## Running the bot and experiments
To train the core model, run:
```
make train-core
```

To run the bot on the commandline, run:
```
make run
```


## Parameters used
Data:
- exclusion percentages: [0, 5, 25, 50, 70, 90, 95, 100]
- augmentation_factor: 0
- runs: 5

Embedding policy:
- epochs: 2000
- attn_shift_range: 5
- embed_dim: 20
- both attentions
- rnn size: 64
- everthing else default

Keras policy:
- binary featurizer/ label token featurizer
- batch size: 32
- rnn size: 64
- epochs: 400
- max history: 38


## Overview of the files
`data/core/train/` - training data from the hotel + restaurant domain
`data/core/test` - test data from the hotel domain
`services` - dummy API services for hotel/restaurant recommendation
`actions.py` - actions file containing the hotel/restaurant search actions
