from __future__ import print_function
from lib2to3.pgen2.token import RPAR
from knn.knn import knn
from popularity.popularity import popularity

import sys

sys.path.append('../')

from functions import haversine
from functions import fifty_pois
from functions import normalize_dic

# almacena las coordenadas de cada poi
pois_coord = {} # id_poi: (latitud, longitud)

# recomendación final de cada poi
recomended = {} # id_poi: rating_hibrido

# rating de cada poi según su distancia con el midpoint
rating = {} # id_poi: rating distancia

# pois que el usuario ya ha visitado
user_pois = []

# lista de distancias al midpoint
dists = []

def hybrid(poi_file, file, out, user_in = '52049'):
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

    with open(file) as train:
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

            if user_in == split[0]:
                user_pois.append(split[1])
                mid_lat += pois_coord[split[1]][0]
                mid_lon += pois_coord[split[1]][1]
                num += 1

    if num != 0:
        mid_point = (mid_lat/num, mid_lon/num)

        for poi in pois_coord.keys():
            dist = haversine(mid_point[0], mid_point[1], pois_coord[poi][0], pois_coord[poi][1])
            # if dist != 0:
            rating[poi] = 1 / dist
            # rating[poi] = 50 - dist

            # else:
            #     rating[poi] = 

    else:
        for poi in pois_coord.keys():
            rating[poi] = 0
    

    hybrid_rec = fifty_pois(rating, user_pois)
    popularity_rec = popularity(file, out)
    knn_rec = knn(file, out)

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


    