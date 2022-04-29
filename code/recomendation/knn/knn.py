import math

# usuario a recomendar
user_in = input("Usuario: ")

# pois que ha visitado el usuario
pois = []

# diccionario con los pois que ha visitado cada usuario y su rating
users_visit = {} # id_user: (id_poi, rating)

# valor de similitud con cada usuario
sim = {} # id_user: similitud

# diccionario con los pois a recomendar
recomended_ny = {} # id_poi: rating
recomended_tk = {}

# Recorremos los 2 ficheros añadiendo a pois los pois que ya ha visitado el usuario
with open('../train_test/US_NewYork/US_NewYork_train.txt') as ny_train:
    for line_ny in ny_train:
        split_ny = line_ny.split("\t")
        # 0: user
        # 1: poi
        # 2: timestamp
        # 3: rating

        # si coincide el usuario dado, añadimos el poi
        if user_in == split_ny[0] and split_ny[1] not in pois:
            pois.append(split_ny[1])

        # si no hemos añadido el usuario que estamos visitando al diccionario lo añadimos
        # con su respectivo poi
        if split_ny[0] not in users_visit.keys():
            users_visit[split_ny[0]] = {split_ny[1]: split_ny[3].strip()}
        # si lo hemos añadido ya, añadimos el poir
        else:
            users_visit[split_ny[0]][split_ny[1]] = split_ny[3].strip()

with open('../train_test/JP_Tokyo/JP_Tokyo_train.txt') as tk_train:
    for line_tk in tk_train:
        split_tk = line_tk.split("\t")
        # 0: user
        # 1: poi
        # 2: timestamp
        # 3: rating

        # si coincide el usuario, añadimos el poi
        if user_in == split_tk[0] and split_tk[1] not in pois:
            pois.append(split_tk[1])

        # si no hemos añadido el usuario que estamos visitando al diccionario lo añadimos
        # con su respectivo poi
        if split_tk[0] not in users_visit.keys():
            users_visit[split_tk[0]] = {split_tk[1]: split_tk[3].strip()}
        # si lo hemos añadido ya, añadimos el poir
        else:
            users_visit[split_tk[0]][split_tk[1]] = split_tk[3].strip()

# recorremos todos los usuario
for user in users_visit.keys():
    num = 0 # numerador de la ecuación de similitud entre usuarios
            # sum(rating1 * rating2)
    
    # por cada poi visitado por el usuario dado
    for poi in pois:     
    # Si también lo ha visitado el usuario que estamos viendo sumamos su producto
        if poi in users_visit[user].keys():
            num += int(users_visit[user][poi]) * int(users_visit[user_in][poi])
           
    a = 0 # sum(ratings_us1^2)
    b = 0 # sum(ratings_us2^2)

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

    

