from functions import read_users

def jaccard(ftest, ftrainG):
    users = read_users(ftest)
    pois = set()

    with open(ftrainG) as train:
        for line in train:
            split = line.split("\t")
            # 0: user
            # 1: poi
            # 2: timestamp
            # 3: rating
            
            pois.add(int(split[1]))

    return users, pois

def all(user, ftrain, gow_pois):
    four_pois = set()

    with open(ftrain) as train:
        for line in train:
            split = line.split("\t")
            # 0: user
            # 1: poi
            # 2: timestamp
            # 3: rating

            if(int(split[0]) == user):
                four_pois.add(int(split[1]))
    
    if len(four_pois) != 0:
        longitud = len(four_pois & gow_pois)/len(four_pois)
    else:
        longitud = 0

    return longitud



if __name__ == "__main__":
    nyF = 'recomendation/train_test/Foursquare/JP_Tokyo/JP_Tokyo_train.txt'
    nyG = 'Gowalla_ratings/JP_Tokyo.txt'
    nytest = 'recomendation/train_test/Foursquare/JP_Tokyo/JP_Tokyo_test.txt'
    
    users, pois = jaccard(nytest, nyG)
    i = 0
    for user in users:
        l = all(user, nyF, pois)
        print(l)

        if l > 0:
            i += 1

    # print(len(users), i, i/len(users))

    nyF = 'segunda_parte/recomendation/train_test/Foursquare/US_SanFrancisco/US_SanFrancisco_train.txt'
    nyG = 'Gowalla_ratings/US_SanFrancisco.txt'
    nytest = 'segunda_parte/recomendation/train_test/Foursquare/US_SanFrancisco/US_SanFrancisco_test.txt'
    

    users, pois = jaccard(nytest, nyG)
    i = 0
    for user in users:
        l = all(user, nyF, pois)

        if l > 0:
            i += 1

    # print(len(users), i, i/len(users))

    nyF = 'recomendation/train_test/Foursquare/US_NewYork/US_NewYork_train.txt'
    nyG = 'Gowalla_ratings/US_NewYork.txt'
    nytest = 'recomendation/train_test/Foursquare/US_NewYork/US_NewYork_test.txt'
    
    users, pois = jaccard(nytest, nyG)
    i = 0
    for user in users:
        l = all(user, nyF, pois)

        if l > 0:
            i += 1
    # print(len(users), i, i/len(users))

  