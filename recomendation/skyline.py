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

    fout_ny_skyline_f = 'users_recomendations/Foursquare/Skyline/NY_Skyline.txt'
    fout_tk_skyline_f = 'users_recomendations/Foursquare/Skyline/TK_Skyline.txt'
    fout_sf_skyline_f = 'users_recomendations/Foursquare/Skyline/SF_Skyline.txt'

    fout_ny_skyline_g = 'users_recomendations/Gowalla/Skyline/NY_Skyline.txt'
    fout_tk_skyline_g = 'users_recomendations/Gowalla/Skyline/TK_Skyline.txt'
    fout_sf_skyline_g = 'users_recomendations/Gowalla/Skyline/SF_Skyline.txt'

    skyline_ny_f = skyline(train_ny_f, test_ny, fout_ny_skyline_f)
    skyline_tk_f = skyline(train_tk_f, test_tk, fout_tk_skyline_f)
    skyline_sf_f = skyline(train_sf_f, test_sf, fout_sf_skyline_f)


    skyline_ny_g = skyline(train_ny_g, test_ny, fout_ny_skyline_g)
    skyline_tk_g = skyline(train_tk_g, test_tk, fout_tk_skyline_g)
    skyline_sf_g = skyline(train_sf_g, test_sf, fout_sf_skyline_g)