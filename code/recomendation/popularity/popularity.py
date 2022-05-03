""" Se encarga de hacer la recomendación al usuario de los 50 pois más populares
según los pois que no ha visitado """

import sys

sys.path.append('../')

from functions import fifty_pois

# suma de ratings de cada poi
rating = {} # id_poi: rating_total

# pois que el usuario ya ha visitado
user_pois = []

def popularity(file, out, user_in = '52049'):
    # Recorremos el fichero añadiendo a pois los pois que ya ha visitado el usuario    
    # y para guardar en el diccionario la suma de los ratings de cada poi
    with open(file) as train:
        for line in train:
            split = line.split("\t")
            # 0: user
            # 1: poi
            # 2: timestamp
            # 3: rating

            # si coincide el usuario, añadimos el poi
            if user_in == split[0] and split[1] not in user_pois:
                user_pois.append(split[1])

            # si hemos visitado el poi, sumamos el rating que hay con el nuevo
            if split[1] in rating.keys():
                rating[split[1]] = int(rating[split[1]]) + int(split[3].strip())
            # si no lo hemos visitado lo guardamos
            else:
                rating[split[1]] = int(split[3].strip())

        return fifty_pois(rating, user_pois)
