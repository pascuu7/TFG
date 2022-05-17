import math

import sys

sys.path.append('../')


from functions import fifty_pois
from functions import sort_recomendations
from functions import read_users
from functions import write_recomendations

# diccionario con los pois que ha visitado cada usuario y su rating
users_visit = {} # id_user: { id_poi1: rating, id_poi2: rating }

# diccionario que guarda la suma de los ratings al cuadrado de cada usuario (denominador de similitud)
user_squared = {} # id_user: (4² + 2² + 3² ...)

set_pois = set()

import time

def data_prepare_knn(ftrain):
    # Recorremos el fichero añadiendo a user_visits los pois que ya ha visitado el usuario
    with open(ftrain) as train:
        for line in train:
            split = line.split("\t")
            # 0: user
            # 1: poi
            # 2: timestamp
            # 3: rating

            # if split[1] not in pois:
            set_pois.add(int(split[1]))

            # si no hemos añadido el usuario que estamos visitando al diccionario lo añadimos
            # con su respectivo poi
            if int(split[0]) not in users_visit:
                users_visit[int(split[0])] = {int(split[1]): int(split[3].strip())}
            # si lo hemos añadido ya, añadimos el poir
            else:
                users_visit[int(split[0])][int(split[1])] = int(split[3].strip())

            # añadimos la el cuadrado del rating a cada poi -> sum(ratings_us1^2) (elemento del denominador similitud)
            if int(split[0]) not in user_squared:
                user_squared[int(split[0])] = int(split[3].strip())**2
            
            else:
                user_squared[int(split[0])] += int(split[3].strip())**2

def all_users_knn(user_test, hybrid, out, k):
    # valor de similitud con cada usuario
    sim = {} # id_user: similitud

    # rating del poi para usuario
    rating = {} # id_poi: rating_total

    if user_test in users_visit:
        user_pois = users_visit[user_test]
    else:
        user_pois = []

    # recorremos todos los usuarios
    for user_train in users_visit:
        if user_test != user_train:
            num = 0. # numerador de la ecuación de similitud entre usuarios
                    # sum(rating1 * rating2)   
            # por cada poi visitado por el usuario dado
            for poi in user_pois:     
            # Si también lo ha visitado el usuario que estamos viendo sumamos su producto
                if poi in users_visit[user_train]:
                    num += users_visit[user_train][poi] * users_visit[user_test][poi]
            if user_train in user_squared and user_test in user_squared:
                
                den = math.sqrt(user_squared[user_train]*user_squared[user_test]) # denominador de la ecuacion de similitud entre usuarios
                                # sqrt(sum(ratings_us1^2) * sum(ratings_us2^2))    
                
                # añadimos al diccionario de similitudes la similitud con ese usuario
                sim[user_train] = num/den

    # SCORE

    similitud = sort_recomendations(sim)
    similitud = similitud[0:k]

    k_neightbours = {}

    for simi in similitud:
        k_neightbours[simi[0]] = simi[1]

    # ahora en similitud tenemos solo los k usuarios con más similitud 

    inicio = time.time()
    for poi in set_pois:
        if poi not in user_pois:
            for user_train in k_neightbours:
                if poi not in rating:
                    if poi in users_visit[user_train]:
                        
                        rating[poi] = (k_neightbours[user_train] * users_visit[user_train][poi])
                    else:
                        rating[poi] = 0
                else:
                    if poi in users_visit[user_train]:
                        rating[poi] += (k_neightbours[user_train] * users_visit[user_train][poi])
                    else:
                        rating[poi] += 0

    

    recomended = fifty_pois(sort_recomendations(rating), user_pois)

    if hybrid:
        return recomended

    else:
        write_recomendations(recomended, user_test, out)
        

# SIMILITUD

def knn(ftrain, ftest, k, out = None, hybrid = False):
    users = read_users(ftest)

    data_prepare_knn(ftrain)

    i = 0
    for user_test in users:
        i += 1
        print(i)
        all_users_knn(user_test, hybrid, out, k)
        

