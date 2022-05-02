import math

# usuario a recomendar
user_in = input("Usuario: ")

# pois que ha visitado el usuario
user_pois = []

# diccionario con los pois que ha visitado cada usuario y su rating
users_visit = {} # id_user: (id_poi, rating)

# valor de similitud con cada usuario
sim = {} # id_user: similitud

# rating del poi para usuario
ny_rating = {} # id_poi: rating_total
tk_rating = {}

# diccionario con los pois a recomendar
recomended_ny = {} # id_poi: rating
recomended_tk = {}

# SIMILITUD

# Recorremos los 2 ficheros añadiendo a pois los pois que ya ha visitado el usuario
with open('../train_test/US_NewYork/US_NewYork_train.txt') as ny_train:
    for line_ny in ny_train:
        split_ny = line_ny.split("\t")
        # 0: user
        # 1: poi
        # 2: timestamp
        # 3: rating

        # si coincide el usuario dado, añadimos el poi
        if user_in == split_ny[0] and split_ny[1] not in user_pois:
            user_pois.append(split_ny[1])

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
        if user_in == split_tk[0] and split_tk[1] not in user_pois:
            user_pois.append(split_tk[1])

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
    for poi in user_pois:     
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

# SCORE

with open('../train_test/US_NewYork/US_NewYork_train.txt') as ny_train:
    for line_ny in ny_train:
        split_ny = line_ny.split("\t")
        # 0: user
        # 1: poi
        # 2: timestamp
        # 3: rating

        if split_ny[1] not in user_pois:
            if split_ny[1] not in ny_rating.keys():
                ny_rating[split_ny[1]] = (sim[split_ny[0]] * int(split_ny[3].strip()))
            # si lo hemos añadido ya, añadimos el poir
            else:
                ny_rating[split_ny[1]] += (sim[split_ny[0]] * int(split_ny[3].strip()))

with open('../train_test/JP_Tokyo/JP_Tokyo_train.txt') as tk_train:
    for line_tk in tk_train:
        split_tk = line_tk.split("\t")
        # 0: user
        # 1: poi
        # 2: timestamp
        # 3: rating


        if split_tk[1] not in user_pois:
            if split_tk[1] not in tk_rating.keys():
                tk_rating[split_tk[1]] = sim[split_tk[0]] * int(split_tk[3].strip())
                # si lo hemos añadido ya, añadimos el poir
            else:
                tk_rating[split_tk[1]] += sim[split_tk[0]] * int(split_tk[3].strip())

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
