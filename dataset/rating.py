""" Se encarga de crear un fichero con los ratings del usuario a cada punto de interés
en función del número de veces que ha visitado ese punto de interés, además selecciona
el último checkin a la hora de guardar el timestamp """

import os

# guardamos en contenido la lista de los ficheros de checkins común (Gowalla y Foursquare)
contenido = os.listdir('city_checkins/')

# diccionarios con el usuario de clave y los checkins correspondientes
dic_timestamp = {}  # id_usuario: (id_poi1 : timestamp1, id_poi2 : timestamp2 ...)
dic_rating = {}  # "id_usuario   id_poi  ciudad.txt": rating

# recorremos los ficheros de checkins para calcular el rating
for name in contenido:
    file = 'city_checkins/' + name

    with open(file) as fcheck:
        for line_check in fcheck:
            split_check = line_check.split("\t")
            # 0: user
            # 1: poi
            # 2: timestamp

            # si el usuario no esta en el diccionario el poi y timestamp que estamos viendo
            if split_check[0] not in dic_timestamp.keys():
                dic_timestamp[split_check[0]] = {split_check[1]: split_check[2].strip()}
            # si el usuario ya se encuentra en el diccionario, añadimos o modificamos el poi que estamos viendo
            else:
                dic_timestamp[split_check[0]][split_check[1]] = split_check[2].strip()

            # clave para guardar en el diccionario de ratings (user poi ciudad.txt)
            key = split_check[0] + '\t' + split_check[1] + '\t' + name

            # si la clave no está en el diccionario la igualamos a 1
            if key not in dic_rating.keys():
                dic_rating[key] = 1
            # si ya se encuentra en el diccionario le sumamos 1
            else:
                dic_rating[key] = dic_rating[key] + 1

# abrimos los 2 ficheros para escribir los checkins con sus ratings
for name in contenido:
    file = 'user_ratings/' + name
    open(file, 'w')

# recorremos el diccionario de ratings
for key in dic_rating:
    split_rat = key.split('\t')
    # 0: id_usuario
    # 1: id_poi
    # 2: ciudad.txt

    name = 'user_ratings/' + split_rat[2].strip()

    # US_NewYork.txt:
    # id_usuario    id_poi_nuestro  timestamp rating
    file = open(name, 'a')
    file.write(str(split_rat[0]) + '\t' + str(split_rat[1]) + '\t' + str(dic_timestamp[split_rat[0]][split_rat[1]]) + '\t' + str(dic_rating[key]) + '\n')
