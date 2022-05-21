from cv2 import norm
from joblib import PrintTime
from knn.knn import all_users_knn, knn
from knn.knn import data_prepare_knn

from popularity.popularity import all_users_pop
from popularity.popularity import data_prepare_pop

import time
import sys

sys.path.append('../')

from functions import haversine
from functions import fifty_pois
from functions import normalize_dic
from functions import sort_recomendations
from functions import read_users
from functions import write_recomendations


def hybrid(poi_file, ftrain, ftest, out, k):

    # almacena las coordenadas de cada poi
    pois_coord = {} # id_poi: (latitud, longitud)

    # guardamos las predicciones de los otros recomendadores
    knn_recomended = {}
    pop_recomended = {}

    users = read_users(ftest)
    city = out.split("/")[3].split("_")[0]
    app = out.split("/")[1]

    file_pop = 'users_recomendations/' + app + '/Popularity/' + city + '_Top50_RepeatedScoreFalse.txt'
    file_knn = 'users_recomendations/' + app + '/Knn/' + city + '_Top50_Knn' + str(k) + '.txt'

    with open(file_pop) as fpop:
        for line_pop in fpop:
            split_pop = line_pop.split("\t")
            # 0: id usuario
            # 1: id poi
            # 2: rating

            if int(split_pop[0]) not in pop_recomended:
                pop_recomended[int(split_pop[0])] = {int(split_pop[1]): int(split_pop[2].strip())} # estaba como [split[1]]
            else:
                pop_recomended[int(split_pop[0])][int(split_pop[1])] =  int(split_pop[2].strip())# estaba como append en vez de add

    with open(file_knn) as fknn:
        for line_knn in fknn:
            split_knn = line_knn.split("\t")
            # 0: id usuario
            # 1: id poi
            # 2: rating

            if int(split_knn[0]) not in knn_recomended:
                knn_recomended[int(split_knn[0])] = {int(split_knn[1]): float(split_knn[2].strip())} # estaba como [split[1]]
            else:
                knn_recomended[int(split_knn[0])][int(split_knn[1])] =  float(split_knn[2].strip())# estaba como append en vez de add 

    with open(poi_file) as poi_file:
        for line_poi in poi_file:
            split_poi = line_poi.split("\t")
            # 0: id poi nuestro
            # 1: id poi foursquare
            # 2: latitud
            # 3: longitud
            # 4: ciudad

            # añadimos en el diccionario las coordenadas de cada poi
            if split_poi[4].strip() == 'US_NewYork':
                pois_coord[int(split_poi[0])] = (float(split_poi[2]), float(split_poi[3]))
            else:
                pois_coord[int(split_poi[0])] = (float(split_poi[2]), float(split_poi[3]))

    i = 0
    for user in users:
        i += 1
        print(i)
        
        # recomendación final de cada poi
        recomended = {} # id_poi: rating_hibrido

        # rating de cada poi según su distancia con el midpoint
        rating = {} # id_poi: rating distancia

        # pois que el usuario ya ha visitado
        user_pois = set()

        inicio = time.time()

        with open(ftrain) as train:
            num = 0
            mid_lat = 0
            mid_lon = 0
            mid_point = 0
            for line in train:
                split = line.split("\t")
                # 0: user
                # 1: poi
                # 2: timestamp
                # 3: rating

                if user == int(split[0]):
                    user_pois.add(int(split[1]))
                    mid_lat += pois_coord[int(split[1])][0]
                    mid_lon += pois_coord[int(split[1])][1]
                    num += 1

        if num != 0:
            mid_point = (mid_lat/num, mid_lon/num)

            for poi in pois_coord:
                if poi not in user_pois:
                    dist = haversine(mid_point[0], mid_point[1], pois_coord[poi][0], pois_coord[poi][1])
                    if dist < 500 and dist > 0:
                        rating[poi] = 1/dist

                    elif dist == 0:
                        rating[poi] = 200

        normalized_popularity = normalize_dic(pop_recomended[user], 'popu ')
        recomended = normalized_popularity

        if user in knn_recomended:
            normalized_knn = normalize_dic(knn_recomended[user], 'knn ')
        else:
            normalized_knn = {}

        for poi in normalized_knn:
            if poi in recomended:
                recomended[poi] += normalized_knn[poi]
            else:
                recomended[poi] = normalized_knn[poi]


        if rating:
            hybrid_rec = fifty_pois(sort_recomendations(rating), user_pois)
            normalized_hybrid = normalize_dic(hybrid_rec, 'hybrid ')

            for poi in normalized_hybrid:
                if poi in recomended:
                    recomended[poi] += normalized_hybrid[poi]
                else:
                    recomended[poi] = normalized_hybrid[poi]

        recomended = fifty_pois(sort_recomendations(recomended), user_pois)

        write_recomendations(recomended, user, out)




    