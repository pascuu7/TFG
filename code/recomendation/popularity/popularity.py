""" Se encarga de hacer la recomendación al usuario de los 50 pois más populares
según los pois que no ha visitado """

import sys

sys.path.append('../')

from functions import fifty_pois

# suma de ratings de cada poi
ny_rating = {} # id_poi: rating_total
tk_rating = {}

# pois que ha visitado el usuario
# visits = {} # id_user: [id_po1, id_poi2, ...]

# pois que el usuario ya ha visitado
user_pois = []

def popularity(file_ny, file_tk, user_in, hybrid):
    # Recorremos los 2 ficheros añadiendo a pois los pois que ya ha visitado el usuario    
    # y para guardar en el diccionario la suma de los ratings de cada poi
    with open(file_ny) as ny_train:
        for line_ny in ny_train:
            split_ny = line_ny.split("\t")
            # 0: user
            # 1: poi
            # 2: timestamp
            # 3: rating

            # si coincide el usuario, añadimos el poi
            if user_in == split_ny[0] and split_ny[1] not in user_pois:
                user_pois.append(split_ny[1])

            # si hemos visitado el poi, sumamos el rating que hay con el nuevo
            if split_ny[1] in ny_rating.keys():
                ny_rating[split_ny[1]] = int(ny_rating[split_ny[1]]) + int(split_ny[3].strip())
            # si no lo hemos visitado lo guardamos
            else:
                ny_rating[split_ny[1]] = int(split_ny[3].strip())

    with open(file_tk) as tk_train:
        for line_tk in tk_train:
            split_tk = line_tk.split("\t")
            # 0: user
            # 1: poi
            # 2: timestamp
            # 3: rating

            # si coincide el usuario, añadimos el poi
            if user_in == split_tk[0] and split_tk[1] not in user_pois:
                user_pois.append(split_tk[1])

            # si hemos visitado el poi, sumamos el rating que hay con el nuevo
            if split_tk[1] in tk_rating.keys():
                tk_rating[split_tk[1]] = int(tk_rating[split_tk[1]]) + int(split_tk[3].strip())
            # si no lo hemos visitado lo guardamos
            else:
                tk_rating[split_tk[1]] = int(split_tk[3].strip())

    if hybrid:
        return fifty_pois(ny_rating, tk_rating, user_pois, False)

    else:
        return fifty_pois(ny_rating, tk_rating, user_pois, True)
