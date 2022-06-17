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
    pop_recomended = {} # user: [poi: score]

    users = read_users(ftest)  # usuarios a recomendar
    city = out.split("/")[3].split("_")[0]  # ciudad que estamos visitando
    app = out.split("/")[1]  # Foursquare o Gowalla

    # recomendador popularidad y knn
    file_pop = 'users_recomendations/' + app + '/Popularity/' + city + '_Top50_RepeatedScoreFalse.txt'
    file_knn = 'users_recomendations/' + app + '/Knn/' + city + '_Top50_Knn' + str(k) + '.txt'

    # guardamos cada recomendación de popularidad en el diccionario
    with open(file_pop) as fpop:
        for line_pop in fpop:
            split_pop = line_pop.split("\t")
            # 0: id usuario
            # 1: id poi
            # 2: score

            if int(split_pop[0]) not in pop_recomended:
                pop_recomended[int(split_pop[0])] = {int(split_pop[1]): int(split_pop[2].strip())} # estaba como [split[1]]
            else:
                pop_recomended[int(split_pop[0])][int(split_pop[1])] =  int(split_pop[2].strip())# estaba como append en vez de add

    # guardamos cada recomendación de knn en el diccionario
    with open(file_knn) as fknn:
        for line_knn in fknn:
            split_knn = line_knn.split("\t")
            # 0: id usuario
            # 1: id poi
            # 2: score

            if int(split_knn[0]) not in knn_recomended:
                knn_recomended[int(split_knn[0])] = {int(split_knn[1]): float(split_knn[2].strip())} # estaba como [split[1]]
            else:
                knn_recomended[int(split_knn[0])][int(split_knn[1])] =  float(split_knn[2].strip())# estaba como append en vez de add 

    # guardamos en otro diccionario las coordenadas de cada poi
    with open(poi_file) as poi_file:
        for line_poi in poi_file:
            split_poi = line_poi.split("\t")
            # 0: id poi nuestro
            # 1: id poi foursquare
            # 2: latitud
            # 3: longitud
            # 4: ciudad

            # añadimos en el diccionario las coordenadas de cada poi
            pois_coord[int(split_poi[0])] = (float(split_poi[2]), float(split_poi[3]))

    for user in users:        
        # recomendación final de cada poi
        recomended = {} # id_poi: rating_hibrido

        # rating de cada poi según su distancia con el midpoint
        rating = {} # id_poi: rating distancia

        # pois que el usuario ya ha visitado
        user_pois = set()

        with open(ftrain) as train:
            num = 0  # número total de pois visitados por un usuario en train
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
                    # sumamos cada latitud y longitud para hacer después la media
                    user_pois.add(int(split[1]))
                    mid_lat += pois_coord[int(split[1])][0]
                    mid_lon += pois_coord[int(split[1])][1]
                    num += 1
        # si ha visitado algo en train
        if num != 0:
            mid_point = (mid_lat/num, mid_lon/num)  # media de coordenadas

            # por cada poi, si el usuario no lo ha visitado calculamos la distancia
            for poi in pois_coord:
                if poi not in user_pois:
                    dist = haversine(mid_point[0], mid_point[1], pois_coord[poi][0], pois_coord[poi][1])
                    if dist < 50 and dist > 0:
                        rating[poi] = 1/dist
                    # si la distancia es 0 le damos un score de 200
                    elif dist == 0:
                        rating[poi] = 200

        # normalizamos el recomendador de popularidad
        normalized_popularity = normalize_dic(pop_recomended[user], 'popu ')
        recomended = normalized_popularity

        # normalizamos el recomendador de knn
        if user in knn_recomended:
            normalized_knn = normalize_dic(knn_recomended[user], 'knn ')
        else:
            normalized_knn = {}

        # sumamos el knn al de popularidad
        for poi in normalized_knn:
            if poi in recomended:
                recomended[poi] += normalized_knn[poi]
            else:
                recomended[poi] = normalized_knn[poi]

        # escogemos los 50 primero de la distancia georgráfica media
        if rating:
            hybrid_rec = fifty_pois(sort_recomendations(rating), user_pois)
            # normalizamos la recomendación
            normalized_hybrid = normalize_dic(hybrid_rec, 'hybrid ')

            # la sumamos a populadidad y knn
            for poi in normalized_hybrid:
                if poi in recomended:
                    recomended[poi] += normalized_hybrid[poi]
                else:
                    recomended[poi] = normalized_hybrid[poi]

        # escogemos los 50 primeros
        recomended = fifty_pois(sort_recomendations(recomended), user_pois)

        # escribimos las recomendaciones
        write_recomendations(recomended, user, out)

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

    poi_file = '../dataset/POI_city.txt'

    # ficheros de salida con las recomendaciones
    fout_hybrid_f = 'users_recomendations/Foursquare/Hybrid/' + pre + '_Top50_knn' + sys.argv[2] + '.txt'
    fout_hybrid_g = 'users_recomendations/Gowalla/Hybrid/' + pre + '_Top50_knn' + sys.argv[2] + '.txt'

    hybrid(poi_file, train_f, test, fout_hybrid_f, sys.argv[2])
    hybrid(poi_file, train_g, test, fout_hybrid_g, sys.argv[2])
