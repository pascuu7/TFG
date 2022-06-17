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
    # guardamos los ficheros train de cada aplicación y test según la ciudad que se indique
    train_f = 'train_test/Foursquare/' + sys.argv[1] + '/' + sys.argv[1] + '_train.txt'
    train_g = 'train_test/Gowalla/' + sys.argv[1] + '/' + sys.argv[1] + '_train.txt'
    test = 'train_test/Gowalla/' + sys.argv[1] + '/' + sys.argv[1] + '_test.txt'

    # guardamos en pre el prefijo del país que se indique
    if sys.argv[1] == "US_SanFrancisco":
        pre = 'SF'

    elif sys.argv[1] == "US_NewYork":
        pre = 'NY'

    else:
        pre = 'TK'

    # ficheros de salida con las recomendaciones
    fout_random_f = 'users_recomendations/Foursquare/Random/' + pre + '_50.txt'
    fout_random_g = 'users_recomendations/Gowalla/Random/' + pre + '_50.txt'

    rand(train_f, test, fout_random_f)
    rand(train_g, test, fout_random_g)
