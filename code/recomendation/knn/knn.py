import math

import sys

sys.path.append('../')

from functions import fifty_pois

# diccionario con los pois que ha visitado cada usuario y su rating
users_visit = {} # id_user: { id_poi1: rating, id_poi2: rating }

# valor de similitud con cada usuario
sim = {} # id_user: similitud

# rating del poi para usuario
rating = {} # id_poi: rating_total

# pois que el usuario ya ha visitado
user_pois = []

# SIMILITUD

def knn(file, out, user_in = '52049'):
    # Recorremos el fichero añadiendo a pois los pois que ya ha visitado el usuario
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

            # si no hemos añadido el usuario que estamos visitando al diccionario lo añadimos
            # con su respectivo poi
            if split[0] not in users_visit.keys():
                users_visit[split[0]] = {split[1]: split[3].strip()}
            # si lo hemos añadido ya, añadimos el poir
            else:
                users_visit[split[0]][split[1]] = split[3].strip()

    # recorremos todos los usuarios
    for user in users_visit.keys():
        num = 0 # numerador de la ecuación de similitud entre usuarios
                # sum(rating1 * rating2)
        
        # por cada poi visitado por el usuario dado
        for poi in user_pois:     
        # Si también lo ha visitado el usuario que estamos viendo sumamos su producto
            if poi in users_visit[user].keys():
                num += int(users_visit[user][poi]) * int(users_visit[user_in][poi])
            
        a = 0 # sum(ratings_us1^2) (elemento del denominador)
        b = 0 # sum(ratings_us2^2) (elemento del denominador)

        # por cada poi visitado por el usuario dado sumamos el rating al cuadrado
        for poi in users_visit[user_in].keys():
            b += int(users_visit[user_in][poi])**2

        # por cada poi visitado por el otro usuario sumamos el rating al cuadrado
        for poi in users_visit[user].keys():
            a += int(users_visit[user][poi])**2
        
        den = math.sqrt(a*b) # denominador de la ecuacion de similitud entre usuarios
                            # sqrt(sum(ratings_us1^2) * sum(ratings_us2^2))

        # añadimos al diccionario de similitudes la similitud con ese usuario
        sim[user] = num/den

    # SCORE

    with open(file) as train:
        for line in train:
            split = line.split("\t")
            # 0: user
            # 1: poi
            # 2: timestamp
            # 3: rating
         
            if split[1] not in rating.keys():
                rating[split[1]] = (sim[split[0]] * int(split[3].strip()))
            # si lo hemos añadido ya, añadimos el poi
            else:
                rating[split[1]] += (sim[split[0]] * int(split[3].strip()))

    
    return fifty_pois(rating, user_pois)

