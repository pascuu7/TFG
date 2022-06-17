import math
import sys

sys.path.append('../')


from functions import fifty_pois
from functions import sort_recomendations
from functions import read_users
from functions import write_recomendations

# diccionario con los pois que ha visitado cada usuario y su rating
users_visit = {}  # id_user: { id_poi1: rating, id_poi2: rating }

# diccionario que guarda la suma de los ratings al cuadrado de cada usuario (denominador de similitud)
user_squared = {}  # id_user: (4² + 2² + 3² ...)

set_pois = set()  # set con todos los pois

def data_prepare_knn(ftrain):
    # Recorremos el fichero añadiendo a user_visits los pois que ya ha visitado el usuario
    with open(ftrain) as train:
        for line in train:
            split = line.split("\t")
            # 0: user
            # 1: poi
            # 2: timestamp
            # 3: rating

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

def all_users_knn(user_test, out, k):
    # valor de similitud con cada usuario
    sim = {}  # id_user: similitud

    # rating del poi para usuario
    rating = {}  # id_poi: rating_total

    # guardamos en user_pois los pois que ha visitado el usuario
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

    # si el usuario tiene similitud on algún usuario
    if sim:
        # seleccionamos los k vecinos con más similitud
        similitud = sort_recomendations(sim)
        similitud = similitud[0:k]

        k_neightbours = {}

        for simi in similitud:
            k_neightbours[simi[0]] = simi[1]  # ususario = similitud

        # recorremos cada punto de interés
        for poi in set_pois:
            # comprobamos que el usuario no ha visitado el poi
            if poi not in user_pois:
                # recorremos los k vecinos del usuario
                for user_train in k_neightbours:
                    # calculamos el score para el poi
                    if poi not in rating:
                        # si el vecino lo ha visitado igualamos a rating * similitud
                        if poi in users_visit[user_train]:
                            rating[poi] = (k_neightbours[user_train] * users_visit[user_train][poi])
                        # si el vecino no lo ha visitado igualamos a 0
                        else:
                            rating[poi] = 0
                    else:
                        # si el vecino lo ha visitado sumamos rating * similitud
                        if poi in users_visit[user_train]:
                            rating[poi] += (k_neightbours[user_train] * users_visit[user_train][poi])
                        # si el vecino no lo ha visitado sumamos 0
                        else:
                            rating[poi] += 0

        
        # cogemos los 50 pois con mayor score
        recomended = fifty_pois(sort_recomendations(rating), user_pois)

        # excribimos las recomendaciones
        write_recomendations(recomended, user_test, out)
        

def knn(ftrain, ftest, k, out = None):
    users = read_users(ftest)

    data_prepare_knn(ftrain)
    i = 0
    for user_test in users:
        i += 1
        print(i)
        all_users_knn(user_test, out, k)


if __name__ == "__main__":
        # Dataset de Foursquare
    train_ny_f = 'train_test/Foursquare/US_NewYork/US_NewYork_train.txt'
    train_tk_f = 'train_test/Foursquare/JP_Tokyo/JP_Tokyo_train.txt'
    train_sf_f = 'train_test/Foursquare/US_SanFrancisco/US_SanFrancisco_train.txt'

    # Dataset de Foursquare + Gowalla
    train_ny_g = 'train_test/Gowalla/US_NewYork/US_NewYork_train.txt'
    train_tk_g = 'train_test/Gowalla/JP_Tokyo/JP_Tokyo_train.txt'
    train_sf_g = 'train_test/Gowalla/US_SanFrancisco/US_SanFrancisco_train.txt'

    # Test (al ser el mismo es indiferente)
    test_ny = 'train_test/Gowalla/US_NewYork/US_NewYork_test.txt'
    test_tk = 'train_test/Gowalla/JP_Tokyo/JP_Tokyo_test.txt'
    test_sf = 'train_test/Gowalla/US_SanFrancisco/US_SanFrancisco_test.txt'

    fout_ny_knn_f = 'users_recomendations/Foursquare/Knn/NY_Top50_Knn' + sys.argv[1] + '.txt'
    fout_tk_knn_f = 'users_recomendations/Foursquare/Knn/TK_Top50_Knn' + sys.argv[1] + '.txt'
    fout_sf_knn_f = 'users_recomendations/Foursquare/Knn/SF_Top50_Knn' + sys.argv[1] + '.txt'

    fout_ny_knn_g = 'users_recomendations/Gowalla/Knn/NY_Top50_Knn' + sys.argv[1] + '.txt'
    fout_tk_knn_g = 'users_recomendations/Gowalla/Knn/TK_Top50_Knn' + sys.argv[1] + '.txt'
    fout_sf_knn_g = 'users_recomendations/Gowalla/Knn/SF_Top50_Knn' + sys.argv[1] + '.txt'
           
    knn(train_ny_f, test_ny, int(sys.argv[1]), out=fout_ny_knn_f)
    knn(train_tk_f, test_tk, int(sys.argv[1]), out=fout_tk_knn_f)
    knn(train_sf_f, test_sf, int(sys.argv[1]), out=fout_sf_knn_f)

    knn(train_ny_g, test_ny, int(sys.argv[1]), out=fout_ny_knn_g)
    knn(train_tk_g, test_tk, int(sys.argv[1]), out=fout_tk_knn_g)
    knn(train_sf_g, test_sf, int(sys.argv[1]), out=fout_sf_knn_g)
