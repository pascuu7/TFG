from knn.knn import knn
from popularity.popularity import popularity

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
                pois_coord[split_poi[0]] = (float(split_poi[2]), float(split_poi[3]))
            else:
                pois_coord[split_poi[0]] = (float(split_poi[2]), float(split_poi[3]))

    for user in users:
        # recomendación final de cada poi
        recomended = {} # id_poi: rating_hibrido

        # rating de cada poi según su distancia con el midpoint
        rating = {} # id_poi: rating distancia

        # pois que el usuario ya ha visitado
        user_pois = []

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

                if user == split[0]:
                    user_pois.append(split[1])
                    mid_lat += pois_coord[split[1]][0]
                    mid_lon += pois_coord[split[1]][1]
                    num += 1

        if num != 0:
            mid_point = (mid_lat/num, mid_lon/num)

            for poi in pois_coord:
                dist = haversine(mid_point[0], mid_point[1], pois_coord[poi][0], pois_coord[poi][1])
                rating[poi] = 50 - dist
        

        hybrid_rec = fifty_pois(rating, user_pois)
        popularity_rec = popularity(ftrain, ftest, hybrid = True)
        knn_rec = knn(ftrain, ftest, k, hybrid = True)

        normalized_popularity = normalize_dic(popularity_rec)
        normalized_knn = normalize_dic(knn_rec)
        normalized_hybrid = normalize_dic(hybrid_rec)

        recomended = normalized_popularity

        for poi in normalized_knn:
            if poi in recomended:
                recomended[poi] += normalized_knn[poi]
            else:
                recomended[poi] = normalized_knn[poi]

        for poi in normalized_hybrid:
            if poi in recomended:
                recomended[poi] += normalized_hybrid[poi]
            else:
                recomended[poi] = normalized_hybrid[poi]


        return fifty_pois(recomended, user_pois)


    