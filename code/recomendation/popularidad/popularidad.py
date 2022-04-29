""" Se encarga de hacer la recomendación al usuario de los 50 pois más populares
según los pois que no ha visitado """

# suma de ratings de cada poi
ny_rating = {} # id_poi: rating_total
tk_rating = {}

# diccionario con los pois a recomendar
recomended_ny = {} # id_poi: rating
recomended_tk = {}

# pois que ha visitado el usuario
# visits = {} # id_user: [id_po1, id_poi2, ...]

# pois que ha visitado el usuario
pois = []

# usuario a recomendar
user_in = input("Usuario: ")

# Recorremos los 2 ficheros añadiendo a pois los pois que ya ha visitado el usuario    
# y para guardar en el diccionario la suma de los ratings de cada poi
with open('../train_test/US_NewYork/US_NewYork_train.txt') as ny_train:
    for line_ny in ny_train:
        split_ny = line_ny.split("\t")
        # 0: user
        # 1: poi
        # 2: timestamp
        # 3: rating


#??????????????????????
        # visits[split_ny[0]].append(split_ny[1])
#?????????????????????? 

        # si coincide el usuario, añadimos el poi
        if user_in == split_ny[0] and split_ny[1] not in pois:
            pois.append(split_ny[1])

        # si hemos visitado el poi, sumamos el rating que hay con el nuevo
        if split_ny[1] in ny_rating.keys():
            ny_rating[split_ny[1]] = int(ny_rating[split_ny[1]]) + int(split_ny[3].strip())
        # si no lo hemos visitado lo guardamos
        else:
            ny_rating[split_ny[1]] = int(split_ny[3].strip())

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

        # si hemos visitado el poi, sumamos el rating que hay con el nuevo
        if split_tk[1] in tk_rating.keys():
            tk_rating[split_tk[1]] = int(tk_rating[split_tk[1]]) + int(split_tk[3].strip())
        # si no lo hemos visitado lo guardamos
        else:
            tk_rating[split_tk[1]] = int(split_tk[3].strip())

# ordenamos los diccionarios de mayor a menor según su rating
sorted_ny = sorted(ny_rating.items(), key=lambda x: x[1], reverse=True)
sorted_tk = sorted(tk_rating.items(), key=lambda x: x[1], reverse=True)

# recorremos el diccionario y por cada poi comprobamos si lo ha visitado el usuario
for poi in sorted_ny:
    # si no lo ha visitado, lo guardamos en el diccionario de recomendados
    if poi not in pois:
        recomended_ny[poi[0]] = poi[1]

    # si ya se ha recomendado 50, paramos
    if len(recomended_ny) == 50:
        break
   
# recorremos el diccionario y por cada poi comprobamos si lo ha visitado el usuario
for poi in sorted_tk:
    # si no lo ha visitado, lo guardamos en el diccionario de recomendados
    if poi not in pois:
        recomended_tk[poi[0]] = poi[1]

    # si ya se ha recomendado 50, paramos
    if len(recomended_tk) == 50:
        break

# print(recomended_ny)
# print(recomended_tk)

# if in_city == 'New York':
#     for poi in ny_rating:
#         if poi not in visits[in_user]:
#             cities.append()