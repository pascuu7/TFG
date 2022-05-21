import os
import sys
import time

from matplotlib import use

sys.path.append('../')

from functions import read_users

# pois que ha visitado el usuario en test
visits = {} # user_id: poi_id

def skyline(ftrain, ftest, out):
    with open(ftest) as test:  
        for line in test:
            split = line.split("\t") 
            # 0: user
            # 1: poi
            # 2: timestamp
            # 3: rating


            if split[0] not in visits:
                visits[split[0]] = set([split[1]])
            else:
                visits[split[0]].add(split[1])

    inicio = time.time()

    i = 0
    for user_test in visits: 
        i += 1
        print(i)  
        if os.path.exists(out):
            with open(out, "a") as fout:
                for poi in visits[user_test]:
                    fout.write(str(user_test) + '\t' + str(poi) + '\n')
                    
        else:
            with open(out, "w") as fout:
                for poi in visits[user_test]:
                    fout.write(str(user_test) + '\t' + str(poi) + '\n')
                    

    fin = time.time()
    # print((fin-inicio))

        


            


