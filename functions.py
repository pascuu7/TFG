import math
import os

def haversine(lat1, lon1, lat2, lon2):
    rad=math.pi/180
    dlat=lat2-lat1
    dlon=lon2-lon1
    R=6372.795477598
    a=(math.sin(rad*dlat/2))**2 + math.cos(rad*lat1)*math.cos(rad*lat2)*(math.sin(rad*dlon/2))**2
    distancia=2*R*math.asin(math.sqrt(a))
    return distancia

def normalize_dic(rating, palabra):  
    maximo = max(rating.values()) # valor máximo del diccionario
    minimo = min(rating.values()) # valor mínimo del diccionario

    # comprobamos que no vaya a ser 0/0
    if maximo != minimo:
        # por cada elemento normalizamos entre 0 y 1 ((valor-mínimo)/(máximo-mínimo))
        for poi in rating:
            rating[poi] = (rating[poi]-minimo) / (maximo-minimo)

    return rating

def sort_recomendations(rating):
    # ordenamos los diccionarios de mayor a menor según su rating
    sort = sorted(rating.items(), key=lambda x: x[1], reverse=True)

    return list(filter(lambda x:x[1] > 0, sort))

def fifty_pois(rating, user_pois):
    # diccionario con los pois a recomendar
    recomended = {} # id_poi: score

    # recorremos el diccionario y por cada poi comprobamos si lo ha visitado el usuario
    for poi in rating:
        # si no lo ha visitado, lo guardamos en el diccionario de recomendados
        if poi[0] not in user_pois:
            recomended[poi[0]] = poi[1]

        if len(recomended) == 50:
            break

    return recomended

def read_users(file):
    users = set()

    with open(file) as test:
        for line in test:
            split = line.split("\t")
            # 0: user
            # 1: poi
            # 2: timestamp
            # 3: rating

            users.add(int(split[0]))

    return users

def user_pois(ffile, user):
    user_pois = set()
    with open(ffile) as file:
        for line in file:
            split = line.split("\t")
            # 0: user
            # 1: poi
            # 2: timestamp
            # 3: rating

            # si coincide el usuario, añadimos el poi
            if user == split[0]:
                user_pois.add(split[1])
    file.close()

    return user_pois

def write_recomendations(recomended, user, out):

    if os.path.exists(out):
        with open(out, "a") as fout:
            for poi in recomended:
                fout.write(str(user) + '\t' + str(poi) + '\t' + str(recomended[poi]) + '\n')
    else:
        with open(out, "w") as fout:
            for poi in recomended:
                fout.write(str(user) + '\t' + str(poi) + '\t' + str(recomended[poi]) + '\n')