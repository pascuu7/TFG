import os
import sys
import time

sys.path.append('../')

from functions import read_users

# pois que ha visitado el usuario en train
user_pois = {} # user_id: poi_id

# pois que ha visitado el usuario en test
visits = {} # user_id: poi_id

def skyline(ftrain, ftest, out):
    users = read_users(ftest)

    with open(ftrain) as train:  
        for line in train:
            split = line.split("\t") 
            user = int(split[0]) # 0: user
            poi = int(split[1]) # 1: poi
            # 2: timestamp
            # 3: rating

            if user not in user_pois:
                user_pois[user] = set(poi)
            else:
                user_pois[user].add(poi)


    with open(ftest) as test:  
        for line in test:
            split = line.split("\t") 
            user = int(split[0]) # 0: user
            poi = int(split[1]) # 1: poi
            # 2: timestamp
            # 3: rating

            if user not in visits:
                visits[user] = set(poi)
            else:
                visits[user].add(poi)

    for user_test in users:
        inicio = time.time()
        if os.path.exists(out):
            with open(out, "a") as fout:
                for poi in visits[user_test][0:50]:
                    if poi not in user_pois:
                        # fout.write(str(user_test) + '\t' + str(poi) + '\n')
                        pass
        else:
            with open(out, "w") as fout:
                for poi in visits[user_test][0:50]:
                    if poi not in user_pois:
                        # fout.write(str(user_test) + '\t' + str(poi) + '\n')
                        pass

        fin = time.time()
        print((fin-inicio)*10000)


            


