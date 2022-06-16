from cgi import print_arguments
import math

from matplotlib import use

from functions import fifty_pois
from functions import sort_recomendations
from functions import read_users
from functions import write_recomendations

# diccionario con los pois que ha visitado cada usuario y su rating
users_visit_four = {} # id_user: { id_poi1: rating, id_poi2: rating }

# diccionario que guarda la suma de los ratings al cuadrado de cada usuario (denominador de similitud)
user_squared_four = {} # id_user: (4² + 2² + 3² ...)

set_pois_four = set()

# diccionario con los pois que ha visitado cada usuario y su rating
users_visit_gow = {} # id_user: { id_poi1: rating, id_poi2: rating }

# diccionario que guarda la suma de los ratings al cuadrado de cada usuario (denominador de similitud)
user_squared_gow = {} # id_user: (4² + 2² + 3² ...)

set_pois_gow = set()

def data_prepare_knn_four(ftrain):
    # Recorremos el fichero añadiendo a user_visits los pois que ya ha visitado el usuario
    with open(ftrain) as train:
        for line in train:
            split = line.split("\t")
            # 0: user
            # 1: poi
            # 2: timestamp
            # 3: rating

            # if split[1] not in pois:
            set_pois_four.add(int(split[1]))

            # si no hemos añadido el usuario que estamos visitando al diccionario lo añadimos
            # con su respectivo poi
            if int(split[0]) not in users_visit_four:
                users_visit_four[int(split[0])] = {int(split[1]): int(split[3].strip())}
            # si lo hemos añadido ya, añadimos el poir
            else:
                users_visit_four[int(split[0])][int(split[1])] = int(split[3].strip())

            # añadimos la el cuadrado del rating a cada poi -> sum(ratings_us1^2) (elemento del denominador similitud)
            if int(split[0]) not in user_squared_four:
                user_squared_four[int(split[0])] = int(split[3].strip())**2
            
            else:
                user_squared_four[int(split[0])] += int(split[3].strip())**2

def data_prepare_knn_gow(ftrain):
    # Recorremos el fichero añadiendo a user_visits los pois que ya ha visitado el usuario
    with open(ftrain) as train:
        for line in train:
            split = line.split("\t")
            # 0: user
            # 1: poi
            # 2: timestamp
            # 3: rating

            # if split[1] not in pois:
            set_pois_gow.add(int(split[1]))

            # si no hemos añadido el usuario que estamos visitando al diccionario lo añadimos
            # con su respectivo poi
            if int(split[0]) not in users_visit_gow:
                users_visit_gow[int(split[0])] = {int(split[1]): int(split[3].strip())}
            # si lo hemos añadido ya, añadimos el poir
            else:
                users_visit_gow[int(split[0])][int(split[1])] = int(split[3].strip())

            # añadimos la el cuadrado del rating a cada poi -> sum(ratings_us1^2) (elemento del denominador similitud)
            if int(split[0]) not in user_squared_gow:
                user_squared_gow[int(split[0])] = int(split[3].strip())**2
            
            else:
                user_squared_gow[int(split[0])] += int(split[3].strip())**2

def all_users_knn(tipo, user_test, k):

    k_neighbours = set() 

    if tipo == 'Four':
        users_visit = users_visit_four
        user_squared = user_squared_four
    else:
        users_visit = users_visit_gow
        user_squared = user_squared_gow
    # valor de similitud con cada usuario
    sim = {} # id_user: similitud

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
                

                if num != 0:
                    # añadimos al diccionario de similitudes la similitud con ese usuario
                    sim[user_train] = num/den

    if sim:

        # SCORE

        similitud = sort_recomendations(sim)
        similitud = similitud[0:k]
        # print(similitud)

        for simi in similitud:
            k_neighbours.add(simi[0])

    return k_neighbours

        

# SIMILITUD

if __name__ == "__main__":
    ftest = 'recomendation/train_test/Foursquare/JP_Tokyo/JP_Tokyo_test.txt'
    ftrain_f = 'recomendation/train_test/Foursquare/JP_Tokyo/JP_Tokyo_train.txt'
    ftrain_g = 'recomendation/train_test/Gowalla/JP_Tokyo/JP_Tokyo_train.txt'
    users = read_users(ftest)

    cambios = {}

    data_prepare_knn_four(ftrain_f)
    data_prepare_knn_gow(ftrain_g)

    k = 100
    i = 0
    coin = 0
    for user_test in users:
        i += 1
        print('momento:', i)
        four = all_users_knn('Four',user_test, k)
        gow = all_users_knn('Gow',user_test, k)

        
        # print(len(four), '\n')
        # print(len(gow), '\n')

        cambios[user_test] = max(len(four), len(gow)) - len(gow & four)

        final = sort_recomendations(cambios)

        if four != gow:
            coin += 1

    print(final[0:10])
    # print(coin, len(users), coin/len(users))
        
        

