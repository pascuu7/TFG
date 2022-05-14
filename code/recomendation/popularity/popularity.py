""" Se encarga de hacer la recomendación al usuario de los 50 pois más populares
según los pois que no ha visitado """

import sys
import os

sys.path.append('../')

from functions import fifty_pois
from functions import sort_recomendations
from functions import read_users
from functions import write_recomendations

# suma de ratings de cada poi
rating = {} # id_poi: rating_total

user_pois = {}

def popularity(ftrain, ftest, repeated = False, out = None, hybrid = False):
    # Recorremos el fichero para guardar en el diccionario 
    # la suma de los ratings de cada poi
    with open(ftrain) as train:
        for line in train:
            split = line.split("\t")
            # 0: user
            # 1: poi
            # 2: timestamp
            # 3: rating

            if split[0] not in user_pois:
                user_pois[split[0]] = set(split[1]) # estaba como [split[1]]
            else:
                user_pois[split[0]].add(split[1]) # estaba como append en vez de add

            if repeated:
                # si hemos visitado el poi, sumamos el rating que hay con el nuevo
                if split[1] in rating:
                    rating[split[1]] = int(rating[split[1]]) + int(split[3].strip())
                # si no lo hemos visitado lo guardamos
                else:
                    rating[split[1]] = int(split[3].strip())
            else:
                if split[1] in rating:
                    rating[split[1]] += 1
                # si no lo hemos visitado lo guardamos
                else:
                    rating[split[1]] = 1
        
    sorted = sort_recomendations(rating)
    users = read_users(ftest)

    train.close()

    i = 0

    for user in users:
        i += 1
        print(i)
        if user in user_pois:
            pois = user_pois[user]
        else:
            pois = []
        
        recomended = fifty_pois(sorted, pois)

        if hybrid:
            return recomended
        else:
            write_recomendations(recomended, user, out)
        