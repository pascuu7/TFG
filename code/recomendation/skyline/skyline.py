import os

def skyline(ftrain, ftest, out):

    # pois que aparecen en train
    train_pois = set()

    # pois que ha visitado el usuario en test
    visits = {} # user_id: poi_id

    with open(ftrain) as train:  
        for line in train:
            split = line.split("\t") 
            # 0: user
            # 1: poi
            # 2: timestamp
            # 3: rating

            train_pois.add(int(split[1]))

    with open(ftest) as test:  
        for line in test:
            split = line.split("\t") 
            # 0: user
            # 1: poi
            # 2: timestamp
            # 3: rating


            if split[0] not in visits:
                visits[int(split[0])] = set([int(split[1])])
            else:
                visits[int(split[0])].add(int(split[1]))

    i = 0
    for user_test in visits: 
        i += 1
        # print(i)  
        if os.path.exists(out):
            with open(out, "a") as fout:
                for poi in visits[user_test]:
                    if poi in train_pois:
                        fout.write(str(user_test) + '\t' + str(poi) + '\n')
                    
        else:
            with open(out, "w") as fout:
                for poi in visits[user_test]:
                    if poi in train_pois:
                        fout.write(str(user_test) + '\t' + str(poi) + '\n')


        


            


