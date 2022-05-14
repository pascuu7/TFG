from cv2 import norm
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

# almacena las coordenadas de cada poi
pois_coord = {} # id_poi: (latitud, longitud)

def hybrid(poi_file, ftrain, ftest, out, k):

    users = read_users(ftest)
    hybrid_popularity = data_prepare_pop(ftrain)
    hybrid_knn = data_prepare_knn(ftrain)

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
        inicio = time.time()
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
                    # print("HAY POI", split[1])
                    user_pois.add(int(split[1]))
                    mid_lat += pois_coord[int(split[1])][0]
                    mid_lon += pois_coord[int(split[1])][1]
                    num += 1
        
        # fin = time.time()
        # print('Calcular elementos ecuacion: ' ,(fin-inicio)*11000, '\n\n')
        # inicio = time.time()
        if num != 0:
            mid_point = (mid_lat/num, mid_lon/num)

            for poi in pois_coord:
                if poi not in user_pois:
                    dist = haversine(mid_point[0], mid_point[1], pois_coord[poi][0], pois_coord[poi][1])
                    if dist < 500:
                        rating[poi] = 1/dist
        
        # fin = time.time()
        # print('Rating: ' ,(fin-inicio)*11000, '\n\n')
        # inicio = time.time()

        popularity_rec = all_users_pop(user, True, out, hybrid_popularity)
        normalized_popularity = normalize_dic(popularity_rec)
        recomended = normalized_popularity

        # fin = time.time()
        # print('Popularity: ' ,(fin-inicio)*11000, '\n\n')
        # inicio = time.time()


        knn_rec = all_users_knn(user, True, out, k)
        # fin = time.time()
        # print('KNN: ' ,(fin-inicio)*11000, '\n\n')
        
        # inicio = time.time()
        if knn_rec:
            normalized_knn = normalize_dic(knn_rec)
        else:
            normalized_knn = {}

        # fin = time.time()
        # print('NORMALIZED KNN: ' ,(fin-inicio)*11000, '\n\n')

        # inicio = time.time()

        for poi in normalized_knn:
            if poi in recomended:
                recomended[poi] += normalized_knn[poi]
            else:
                recomended[poi] = normalized_knn[poi]

        if rating:
            hybrid_rec = fifty_pois(sort_recomendations(rating), user_pois)
            normalized_hybrid = normalize_dic(hybrid_rec)

            for poi in normalized_hybrid:
                if poi in recomended:
                    recomended[poi] += normalized_hybrid[poi]
                else:
                    recomended[poi] = normalized_hybrid[poi]

        # fin = time.time()
        # print('Recomended: ' ,(fin-inicio)*11000, '\n\n')
        # inicio = time.time()

        recomended = fifty_pois(sort_recomendations(recomended), user_pois)
        # fin = time.time()
        # print('Final: ' ,(fin-inicio)*11000, '\n\n')

        print(user, recomended, '\n\n')

        

        # write_recomendations(recomended, user, out)




    