import os
import sys

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

            if int(split[0]) not in visits:
                visits[int(split[0])] = set([int(split[1])])
            else:
                visits[int(split[0])].add(int(split[1]))

    # por cada usuario de test
    for user_test in visits:  
        if os.path.exists(out):
            with open(out, "a") as fout:
                # escribimos todos los pois que visitan en test siempre y cuando estén en train
                for poi in visits[user_test]:
                    if poi in train_pois:
                        fout.write(str(user_test) + '\t' + str(poi) + '\n')
                    
        else:
            with open(out, "w") as fout:
                for poi in visits[user_test]:
                    if poi in train_pois:
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
    fout_skyline_f = 'users_recomendations/Foursquare/Skyline/' + pre + '_Skyline.txt'
    fout_skyline_g = 'users_recomendations/Gowalla/Skyline/' + pre + '_Skyline.txt'

    skyline(train_f, test, fout_skyline_f)
    skyline(train_g, test, fout_skyline_g)