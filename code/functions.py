import math

def haversine(lat1, lon1, lat2, lon2):
    rad=math.pi/180
    dlat=lat2-lat1
    dlon=lon2-lon1
    R=6372.795477598
    a=(math.sin(rad*dlat/2))**2 + math.cos(rad*lat1)*math.cos(rad*lat2)*(math.sin(rad*dlon/2))**2
    distancia=2*R*math.asin(math.sqrt(a))
    return distancia

def fifty_pois(ny_rating, tk_rating, user_pois):
    # diccionario con los pois a recomendar
    recomended_ny = {} # id_poi: rating
    recomended_tk = {}

    # ordenamos los diccionarios de mayor a menor según su rating
    sorted_ny = sorted(ny_rating.items(), key=lambda x: x[1], reverse=True)
    sorted_tk = sorted(tk_rating.items(), key=lambda x: x[1], reverse=True)

    # recorremos el diccionario y por cada poi comprobamos si lo ha visitado el usuario
    for poi in sorted_ny:
        # si no lo ha visitado, lo guardamos en el diccionario de recomendados
        if poi not in user_pois:
            recomended_ny[poi[0]] = poi[1]

        # si ya se ha recomendado 50, paramos
        if len(recomended_ny) == 50:
            break
    
    # recorremos el diccionario y por cada poi comprobamos si lo ha visitado el usuario
    for poi in sorted_tk:
        # si no lo ha visitado, lo guardamos en el diccionario de recomendados
        if poi not in user_pois:
            recomended_tk[poi[0]] = poi[1]

        # si ya se ha recomendado 50, paramos
        if len(recomended_tk) == 50:
            break

    return recomended_ny, recomended_tk