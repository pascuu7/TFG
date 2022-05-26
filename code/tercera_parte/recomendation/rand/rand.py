import random
import sys
import os

sys.path.append('../')

from functions import read_users

def rand(ftrain, ftest, out):
    users = read_users(ftest)
    pois = set()
    with open(ftrain) as train:
        for line in train:
            split = line.split("\t")
            # 0: user
            # 1: poi
            # 2: timestamp
            # 3: rating

            pois.add(int(split[1]))

    rand_list = list(pois)

    i = 0
    for user_test in users:
        i += 1

        print(i)
        random.shuffle(rand_list)
        
        if os.path.exists(out):
            with open(out, "a") as fout:
                for poi in rand_list[0:50]:
                    fout.write(str(user_test) + '\t' + str(poi) + '\n')
        else:
            with open(out, "w") as fout:
                for poi in rand_list[0:50]:
                    fout.write(str(user_test) + '\t' + str(poi) + '\n')




