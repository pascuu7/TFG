import random
import sys
import os

sys.path.append('../')

from functions import read_users

def rand(ftrain, ftest, out):
    # usuarios de test
    users = read_users(ftest)
    pois = set()  # todos los pois de train
    with open(ftrain) as train:
        for line in train:
            split = line.split("\t")
            # 0: user
            # 1: poi
            # 2: timestamp
            # 3: rating

            pois.add(int(split[1]))

    rand_list = list(pois)

    # por cada usuario
    for user_test in users:
        # movemos todos los elementos de la lista de forma aleatoria
        random.shuffle(rand_list)
        
        # escribimos los primeros 50 elementos de la lista
        if os.path.exists(out):
            with open(out, "a") as fout:
                for poi in rand_list[0:50]:
                    fout.write(str(user_test) + '\t' + str(poi) + '\n')
        else:
            with open(out, "w") as fout:
                for poi in rand_list[0:50]:
                    fout.write(str(user_test) + '\t' + str(poi) + '\n')



if __name__ == "__main__":
        # Dataset de Foursquare
    train_ny_f = 'train_test/Foursquare/US_NewYork/US_NewYork_train.txt'
    train_tk_f = 'train_test/Foursquare/JP_Tokyo/JP_Tokyo_train.txt'
    train_sf_f = 'train_test/Foursquare/US_SanFrancisco/US_SanFrancisco_train.txt'

    # Dataset de Foursquare + Gowalla
    train_ny_g = 'train_test/Gowalla/US_NewYork/US_NewYork_train.txt'
    train_tk_g = 'train_test/Gowalla/JP_Tokyo/JP_Tokyo_train.txt'
    train_sf_g = 'train_test/Gowalla/US_SanFrancisco/US_SanFrancisco_train.txt'

    # Test (al ser el mismo es indiferente)
    test_ny = 'train_test/Gowalla/US_NewYork/US_NewYork_test.txt'
    test_tk = 'train_test/Gowalla/JP_Tokyo/JP_Tokyo_test.txt'
    test_sf = 'train_test/Gowalla/US_SanFrancisco/US_SanFrancisco_test.txt'

    fout_ny_random_f = 'users_recomendations/Gowalla/Random/NY_50.txt'
    fout_tk_random_f = 'users_recomendations/Gowalla/Random/TK_50.txt'
    fout_sf_random_f = 'users_recomendations/Gowalla/Random/SF_50.txt'

    fout_ny_random_g = 'users_recomendations/Gowalla/Random/NY_50.txt'
    fout_tk_random_g = 'users_recomendations/Gowalla/Random/TK_50.txt'
    fout_sf_random_g = 'users_recomendations/Gowalla/Random/SF_50.txt'

    random_ny_f = rand(train_ny_f, test_ny, fout_ny_random_f)
    random_tk_f = rand(train_tk_f, test_tk, fout_tk_random_f)
    random_tk_f = rand(train_sf_f, test_sf, fout_sf_random_f)

    random_ny_g = rand(train_ny_g, test_ny, fout_ny_random_g)
    random_tk_g = rand(train_tk_g, test_tk, fout_tk_random_g)
    random_tk_g = rand(train_sf_g, test_sf, fout_sf_random_g)