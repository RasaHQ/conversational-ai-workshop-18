import numpy as np
import matplotlib.pyplot as plt
# import seaborn as sns
# import pandas as pd


import pickle

# restaurant present
chitchat = pickle.load(open('hotel_chitchat.p', 'rb'))

# latest, sparse attention

chitchat = pickle.load(open('experiments_0505/hotel_chitchat.p', 'rb'))

# new data
chitchat = pickle.load(open('experiments_0805/hotel_chitchat.p', 'rb'))

# restaurant not present
chitchat_no = pickle.load(open('hotel_noresto_chitchat.p', 'rb'))

# restaurant present epochs 4000, embed dim 20


correction = {'no_of_stories': [25.0, 24.0, 19.0, 13.0, 8.0, 3.0, 1.0, 0.0],
              'embed': [[24, 24, 23, 17, 16, 7, 8, 6], [24, 24, 22, 18, 16, 7, 8, 5], [24, 24, 23, 19, 17, 9, 7, 9]],
              'keras': [[23, 24, 18, 14, 10, 4, 3, 0], [22, 21, 18, 14, 11, 4, 3, 0], [24, 21, 19, 14, 11, 4, 3, 0]]}

# latest, sparse attention
correction = pickle.load(open('experiments_0505/hotel_correction.p', 'rb'))

# new data
correction = pickle.load(open('experiments_0805/hotel_correction.p', 'rb'))
# restaurant present

didthatwork = pickle.load(open('hotel_didthatwork.p', 'rb'))

# latest, sparse attention
didthatwork = pickle.load(open('experiments_0505/hotel_didthatwork.p', 'rb'))

# new data
didthatwork = pickle.load(open('experiments_0805/hotel_didthatwork.p', 'rb'))

# restaurant not present

didthatwork_no = pickle.load(open('hotel_noresto_didthatwork.p', 'rb'))

# restaurant present 4000 epochs, 20 embed dim

explain = {'no_of_stories': [25.0, 24.0, 19.0, 13.0, 8.0, 3.0, 1.0, 0.0],
           'embed': [[25, 25, 24, 19, 17, 9, 10, 9], [25, 25, 23, 21, 20, 11, 10, 10], [25, 25, 23, 19, 18, 10, 12, 11]],
           'keras': [[25, 25, 20, 15, 13, 5, 5, 0], [25, 22, 20, 15, 13, 4, 6, 0], [25, 22, 22, 14, 14, 3, 6, 1]]}

# latest, sparse attention
explain = pickle.load(open('experiments_0505/hotel_explain.p', 'rb'))

# new data
explain = pickle.load(open('experiments_0805/hotel_explain.p', 'rb'))

# restaurant not present


explain_no = pickle.load(open('hotel_noresto_explain.p', 'rb'))


# percentages = [0, 5, 25, 50, 70, 90, 95, 100]
# percentages = [70, 90, 95, 100]
# percentages = [100-x for x in percentages]
memo = [x/30.0 for x in didthatwork_no['no_of_stories']]


embed = np.mean(didthatwork_no['embed'], axis=0)
embed_std = np.std(didthatwork_no['embed'], axis=0)

embed = [x/30.0 for x in embed]

embed_std = [x/30.0 for x in embed_std]

# embed_noattn = np.mean(didthatwork_no['embed_noattn'], axis=0)
# embed_noattn_std = np.std(didthatwork_no['embed_noattn'], axis=0)
#
# embed_noattn = [x/25.0 for x in embed_noattn]
#
# embed_noattn_std = [x/25.0 for x in embed_noattn_std]


keras = np.mean(didthatwork_no['keras'], axis=0)
keras = [x/30.0 for x in keras]
keras_std = np.std(didthatwork_no['keras'],axis=0)
keras_std = [x/30.0 for x in keras_std]
# print(embed)

plt.plot(didthatwork_no['no_of_stories'], keras, label='keras', marker='.', color='#6b2def')
plt.fill_between(didthatwork_no['no_of_stories'], [x-y for x,y in zip(keras,keras_std)], [x+y for x,y in zip(keras,keras_std)], color='#6b2def', alpha=0.2)
plt.plot(didthatwork_no['no_of_stories'], embed, label='embed', marker='.', color='#f22e4e')
plt.fill_between(didthatwork_no['no_of_stories'], [x-y for x,y in zip(embed,embed_std)], [x+y for x,y in zip(embed,embed_std)], color='#f22e4e', alpha=0.2)
# plt.plot(didthatwork_no['no_of_stories'], embed_noattn, label='embed (no attention)', marker='.', color='#42f48c')
# plt.fill_between(didthatwork_no['no_of_stories'], [x-y for x,y in zip(embed_noattn,embed_noattn_std)], [x+y for x,y in zip(embed_noattn,embed_noattn_std)], color='#42f48c', alpha=0.2)
plt.plot(didthatwork_no['no_of_stories'], memo, '--', label='memoization', color='#727272')
plt.xlabel('number of stories present')
plt.ylabel('accuracy')
plt.xlim([0.0, 30.0])
plt.ylim([0, 1.02])

plt.legend(loc=4)
plt.savefig('graphs/newest/didthatwork_no.pdf', format='pdf')
plt.show()
