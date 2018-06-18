import numpy as np
import matplotlib.pyplot as plt
# import seaborn as sns
# import pandas as pd


import pickle

# restaurant present
results = pickle.load(open('data-simulated/simulated_hotel_train.p', 'rb'))


# percentages = [0, 5, 25, 50, 70, 90, 95, 100]
# percentages = [70, 90, 95, 100]
# percentages = [100-x for x in percentages]
no_of_stories = results['no_of_stories']

print(results)


embed = np.mean(results['embed'], axis=0)
embed_std = np.std(results['embed'], axis=0)

# embed = [x/30.0 for x in embed]
# embed_std = [x/30.0 for x in embed_std]

embed_noattn_before = np.mean(results['embed_no_attn_before'], axis=0)
embed_noattn_before_std = np.std(results['embed_no_attn_before'], axis=0)

# embed_noattn_before = [x/30.0 for x in embed_noattn_before]
# embed_noattn_before_std = [x/30.0 for x in embed_noattn_before_std]

embed_noattn_after = np.mean(results['embed_no_attn_after'], axis=0)
embed_noattn_after_std = np.std(results['embed_no_attn_after'], axis=0)

# embed_noattn_after = [x/30.0 for x in embed_noattn_after]
# embed_noattn_after_std = [x/30.0 for x in embed_noattn_after_std]

embed_noattn = np.mean(results['embed_no_attn'], axis=0)
embed_noattn_std = np.std(results['embed_no_attn'], axis=0)

# embed_noattn = [x/30.0 for x in embed_noattn]
# embed_noattn_std = [x/30.0 for x in embed_noattn_std]

# print(embed)

plt.plot(results['no_of_stories'], embed, label='embed', marker='.', color='#f22e4e')
plt.fill_between(results['no_of_stories'], [x-y for x,y in zip(embed,embed_std)], [x+y for x,y in zip(embed,embed_std)], color='#f22e4e', alpha=0.2)

plt.plot(results['no_of_stories'], embed_noattn_before, label='embed_noattn_before', marker='.', color='#6b2def')
plt.fill_between(results['no_of_stories'], [x-y for x,y in zip(embed_noattn_before,embed_noattn_before_std)], [x+y for x,y in zip(embed_noattn_before,embed_noattn_before_std)], color='#6b2def', alpha=0.2)

plt.plot(results['no_of_stories'], embed_noattn_after, label='embed_noattn_after', marker='.', color='#42f48c')
plt.fill_between(results['no_of_stories'], [x-y for x,y in zip(embed_noattn_after,embed_noattn_after_std)], [x+y for x,y in zip(embed_noattn_after,embed_noattn_after_std)], color='#42f48c', alpha=0.2)

plt.plot(results['no_of_stories'], embed_noattn, label='embed (no attention)', marker='.', color='#727272')
plt.fill_between(results['no_of_stories'], [x-y for x,y in zip(embed_noattn,embed_noattn_std)], [x+y for x,y in zip(embed_noattn,embed_noattn_std)], color='#727272', alpha=0.2)

# plt.plot(didthatwork_no['no_of_stories'], memo, '--', label='memoization', color='#727272')
plt.xlabel('number of stories present')
plt.ylabel('accuracy')
# plt.xlim([0.0, 30.0])
# plt.ylim([0, 1.02])

plt.legend(loc=0)
plt.savefig('embed_ablation.pdf', format='pdf')
plt.show()
