from knn.knn import knn
from popularity.popularity import popularity

import sys

sys.path.append('../')

from functions import haversine
from functions import fifty_pois

# almacena las coordenadas de cada poi
pois_coord_ny = {} # id_poi: (latitud, longitud)
pois_coord_tk = {}

# recomendación final de cada poi
recomended_ny = {} # id_poi: rating hibrido
recomended_tk = {}

# pois que el usuario ya ha visitado
user_pois = []

# rating de cada poi según su distancia con el midpoint
ny_rating = {} # id_poi: rating distancia
tk_rating = {}

def hybrid(poi_file, file_ny, file_tk, user_in):
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
                pois_coord_ny[split_poi[0]] = (float(split_poi[2]), float(split_poi[3]))
            else:
                pois_coord_tk[split_poi[0]] = (float(split_poi[2]), float(split_poi[3]))

    with open(file_ny) as ny_train:
        num = 0
        mid_lat = 0
        mid_lon = 0
        mid_point = 0
        for line_ny in ny_train:
            split_ny = line_ny.split("\t")
            # 0: user
            # 1: poi
            # 2: timestamp
            # 3: rating

            if user_in == split_ny[0]:
                user_pois.append(split_ny[1])
                # print(pois_coord_ny[split_ny[1]])
                mid_lat += pois_coord_ny[split_ny[1]][0]
                mid_lon += pois_coord_ny[split_ny[1]][1]
                num += 1

    # print(mid_ny_lat/num, mid_ny_lon/num)
    # print(pois_coord)
    # print(haversine(mid_ny_lat/num, mid_ny_lon/num, 40.759155, -73.970572))
    if num != 0:
        mid_point = (mid_lat/num, mid_lon/num)

        for poi in pois_coord_ny.keys():
            dist = haversine(mid_point[0], mid_point[1], pois_coord_ny[poi][0], pois_coord_ny[poi][1])
            # print(dist)
            # print(mid_point[0], mid_point[1], pois_coord_ny[poi][0], pois_coord_ny[poi][1])
            ny_rating[poi] = 50 - dist

    else:
        for poi in pois_coord_ny.keys():
            ny_rating[poi] = 0
    

    with open(file_tk) as tk_train:
        num = 0
        mid_lat = 0
        mid_lon = 0
        mid_point = 0
        for line_tk in tk_train:
            split_tk = line_tk.split("\t")
            # 0: user
            # 1: poi
            # 2: timestamp
            # 3: rating

            if user_in == split_tk[0]:
                user_pois.append(split_tk[1])
                mid_lat += pois_coord_tk[split_tk[1]][0]
                mid_lon += pois_coord_tk[split_tk[1]][1]
                num += 1
    
    if num != 0:
        mid_point = (mid_lat/num, mid_lon/num)


        for poi in pois_coord_tk.keys():
            dist = haversine(mid_point[0], mid_point[1], pois_coord_tk[poi][0], pois_coord_tk[poi][1])
            tk_rating[poi] = 100 - dist

    else:
        for poi in pois_coord_tk.keys():
            tk_rating[poi] = 0


    hybryd_ny, hybryd_tk = fifty_pois(ny_rating, tk_rating, user_pois, False)
    popularity_ny, popularity_tk = popularity(file_ny, file_tk, user_in, True)
    knn_ny, knn_tk = knn(file_ny, file_tk, user_in, True)

    for poi in pois_coord_ny:
        if poi not in user_pois:
            recomended_ny[poi] = knn_ny[poi]

    for poi in pois_coord_tk:
        if poi not in user_pois:
            recomended_tk[poi] = 0


    print(fifty_pois(ny_rating, tk_rating, user_pois, True))

    