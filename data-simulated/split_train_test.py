import random
import io

filename = "all_hotel_simulated.md"
ls = open(filename).readlines()
stories = []
test_frac = 0.25

for l in ls:
    if l.startswith("##"):
        stories.append([])
    stories[-1].append(l)


random.shuffle(stories)
n_train = len(stories) - round(test_frac*len(stories))

l_train = []
l_test = []
for s in stories[:n_train]:
    for l in s:
        l_train.append(l)

for s in stories[n_train:]:
    for l in s:
        l_test.append(l)


with io.open("simulated_hotel_train.md",'w') as f:
    f.writelines(l_train)

with io.open("simulated_hotel_test.md",'w') as f:
    f.writelines(l_test)

