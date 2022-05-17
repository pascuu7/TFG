""" Se encarga de hacer la recomendación al usuario de los 50 pois más populares
según los pois que no ha visitado """

import sys

sys.path.append('../')

from functions import fifty_pois
from functions import sort_recomendations
from functions import read_users
from functions import write_recomendations

# suma de ratings de cada poi
rating = {} # id_poi: rating_total

# pois que han visitado los usuarios
user_visits = {} # id_user: { id_poi1: rating, id_poi2: rating }

def data_prepare_pop(ftrain, repeated = False):
    

    # Recorremos el fichero para guardar en el diccionario 
    # la suma de los ratings de cada poi
    with open(ftrain) as train:
        for line in train:
            split = line.split("\t")
            # 0: user
            # 1: poi
            # 2: timestamp
            # 3: rating

            if int(split[0]) not in user_visits:
                user_visits[int(split[0])] = set([int(split[1])]) # estaba como [split[1]]
            else:
                user_visits[int(split[0])].add(int(split[1])) # estaba como append en vez de add

            if repeated:
                # si hemos visitado el poi, sumamos el rating que hay con el nuevo
                if int(split[1]) in rating:
                    rating[int(split[1])] = int(rating[int(split[1])]) + int(split[3].strip())
                # si no lo hemos visitado lo guardamos
                else:
                    rating[int(split[1])] = int(split[3].strip())
            else:
                if int(split[1]) in rating:
                    rating[int(split[1])] += 1
                # si no lo hemos visitado lo guardamos
                else:
                    rating[int(split[1])] = 1
        
    sorted = sort_recomendations(rating)
    
    train.close()

    return sorted

def all_users_pop(user, hybrid, out, sorted):
    if user in user_visits:
        user_pois = user_visits[user]
    else:
        user_pois = set()

    recomended = fifty_pois(sorted, user_pois)

    if hybrid:
        return recomended
    else:     
        write_recomendations(recomended, user, out)
        


def popularity(ftrain, ftest, repeated = False, out = None, hybrid = False):
    
    
    sorted = data_prepare_pop(ftrain, repeated)
    users = read_users(ftest)

    i = 0

    for user in users:
        i += 1
        # print(i)
        all_users_pop(user, hybrid, out, sorted)

        # fin = time.time()
        # print('Recomended: ' ,(fin-inicio)*11000, '\n\n')
        