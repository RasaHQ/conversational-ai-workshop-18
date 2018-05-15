import numpy as np
import matplotlib.pyplot as plt
import pickle

def plot_curve(filename, ax=None, **kwargs):
    ax = ax or plt.gca()
    data = pickle.load(open(filename, 'rb'))
    x = data["no_of_stories"]
    for label in ['keras', 'embed']:
        if len(data[label]) == 0:
            continue
        mean = np.mean(data[label], axis=0)
        std = np.std(data[label], axis=0)
        ax.plot(x, mean, label=label, marker='.')
        ax.fill_between(x,
                        [m-s for m,s in zip(mean,std)],
                        [m+s for m,s in zip(mean,std)],
                        color='#6b2def',
                        alpha=0.2)

    #ax.set_ylim([0, 25])
    ax.legend(loc=4)

ax = plt.subplot(111)
filename='/Users/alan/Developer/dialog/research/generalisation-bot/simulated_hotel_train.p'
plot_curve(filename, ax)
plt.show()
