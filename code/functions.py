import math

def haversine(lat1, lon1, lat2, lon2):
    rad=math.pi/180
    dlat=lat2-lat1
    dlon=lon2-lon1
    R=6372.795477598
    a=(math.sin(rad*dlat/2))**2 + math.cos(rad*lat1)*math.cos(rad*lat2)*(math.sin(rad*dlon/2))**2
    distancia=2*R*math.asin(math.sqrt(a))
    return distancia


def normalize_dic(rating):  
    maximo = max(rating.values()) # valor máximo del diccionario
    minimo = min(rating.values()) # valor mínimo del diccionario

    # comprobamos que no vaya a ser 0/0
    if maximo != minimo:
        # por cada elemento normalizamos entre 0 y 1 ((valor-mínimo)/(máximo-mínimo))
        for poi in rating.keys():
            rating[poi] = (rating[poi]-minimo) / (maximo-minimo)

    return rating

def fifty_pois(rating, user_pois):
    # diccionario con los pois a recomendar
    recomended = {} # id_poi: score

    # ordenamos los diccionarios de mayor a menor según su rating
    sort = sorted(rating.items(), key=lambda x: x[1], reverse=True)

    # recorremos el diccionario y por cada poi comprobamos si lo ha visitado el usuario
    for poi in sort:
        # si no lo ha visitado, lo guardamos en el diccionario de recomendados
        if poi not in user_pois:
            recomended[poi[0]] = poi[1]

        # si ya se ha recomendado 50, paramos
        if len(recomended) == 50:
            break

    return recomended