import numpy as np
import matplotlib.pyplot as plt

# restaurant present
# chitchat = {'no_of_stories': [30.0, 29.0, 23.0, 15.0, 9.0, 3.0, 1.0, 0.0],
#             'embed': [[30, 30, 29, 28, 24, 13, 15, 0], [30, 30, 29, 29, 22, 14, 9, 4], [30, 30, 29, 25, 25, 16, 11, 8]],
#             'keras': [[30, 26, 25, 21, 21, 7, 4, 0], [28, 28, 28, 18, 22, 9, 8, 1], [30, 30, 28, 23, 18, 8, 5, 0]]}

chitchat = {'no_of_stories': [9.0, 3.0, 2.0, 0.0],
            'embed': [[26, 19, 13, 6], [24, 18, 11, 0], [27, 16, 21, 8]],
            'keras': [[18, 9, 4, 0], [18, 8, 3, 0], [20, 9, 9, 0]]}

# restaurant not present
# chitchat = {u'no_of_stories': [30.0, 29.0, 23.0, 15.0, 9.0, 3.0, 1.0, 0.0], u'embed': [[30, 29, 26,
#  23, 18, 5, 2, 0], [30, 28, 27, 21, 19, 4, 2, 0], [30, 29, 27, 21, 17, 4, 2, 0]], u'keras': [[30, 28, 26, 20, 16, 4
# , 2, 0], [30, 29, 26, 20, 15, 4, 2, 0], [30, 29, 26, 20, 15, 4, 2, 0]]}

# # restaurant present
# correction = {'no_of_stories': [8.0, 3.0, 1.0, 0.0],
#               'embed': [[0, 2, 2, 0], [4, 3, 1, 0], [3, 5, 7, 0]],
#               'keras': [[11, 4, 3, 0], [11, 5, 3, 0], [11, 6, 3, 0]]}

correction = {'no_of_stories': [8.0, 3.0, 1.0, 0.0],
             'embed': [[8, 4, 3, 2], [10, 5, 3, 0], [6, 5, 1, 0]],
             'keras': [[12, 4, 3, 0], [11, 3, 3, 0], [11, 4, 3, 0]]}

# restaurant not present
# correction = {'no_of_stories': [8.0, 3.0, 1.0, 0.0],
#               'embed': [[5, 1, 1, 0], [4, 1, 0, 0], [3, 0, 0, 0]],
#               'keras': [[9, 2, 1, 0], [9, 2, 1, 0], [9, 2, 1, 0]]}

# restaurant present
# didthatwork = {'no_of_stories': [9.0, 3.0, 2.0, 0.0],
#                'embed': [[26, 18, 7, 1], [27, 22, 13, 12], [24, 18, 9, 4]],
#                'keras': [[20, 8, 3, 0], [17, 7, 3, 0], [20, 6, 5, 0]]}

didthatwork = {'no_of_stories': [9.0, 3.0, 2.0, 0.0],
               'embed': [[28, 16, 17, 14], [22, 16, 18, 8], [24, 17, 14, 9]],
               'keras': [[22, 9, 8, 0], [19, 7, 9, 0], [20, 9, 4, 1]]}

# restaurant not present
# didthatwork = {'no_of_stories': [9.0, 3.0, 2.0, 0.0],
#                'embed': [[18, 4, 2, 0], [18, 4, 2, 0], [17, 4, 2, 0]],
#                'keras': [[16, 4, 2, 0], [17, 4, 2, 0], [15, 4, 2, 0]]}


# restaurant present
# explain = {'no_of_stories': [3.0, 1.0, 1.0, 0.0],
#            'embed': [[8, 5, 9, 0], [8, 8, 10, 0], [8, 9, 13, 4]],
#            'keras': [[6, 4, 0, 0], [8, 2, 2, 0], [7, 6, 1, 0]]}
explain = {'no_of_stories': [3.0, 1.0, 1.0, 0.0],
           'embed': [[13, 10, 8, 5], [11, 11, 8, 7], [9, 5, 8, 3]],
           'keras': [[5, 4, 3, 0], [4, 8, 5, 2], [6, 7, 9, 1]]}


# restaurant not present

# explain = {'no_of_stories': [3.0, 1.0, 1.0, 0.0],
#            'embed': [[4, 5, 5, 0], [4, 1, 4, 0], [5, 5, 5, 0]],
#            'keras': [[2, 0, 0, 0], [2, 0, 0, 0], [2, 0, 0, 0]]}

# percentages = [0, 5, 25, 50, 70, 90, 97, 100]
percentages = [70, 90, 95, 100]
percentages = [100-x for x in percentages]
memo = [x/100.0 for x in percentages]

embed = np.mean(chitchat['embed'], axis=0)
embed = [x/30.0 for x in embed]
keras = np.mean(chitchat['keras'], axis=0)
keras = [x/30.0 for x in keras]
print(embed)

plt.plot(percentages, keras, label='keras', marker='.')
plt.plot(percentages, embed, label='embed', marker='.')
plt.plot(percentages, memo, '--', label='memoization')
plt.xlabel('percentage of data present')
plt.ylabel('accuracy')
plt.xlim([0, 30])
plt.ylim([0, 0.95])

plt.legend(loc=4)
plt.show()
