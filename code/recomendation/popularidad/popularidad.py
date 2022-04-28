""" Se encarga de hacer la recomendación al usuario de los 50 pois más populares
según los pois que no ha visitado """

from genericpath import exists
import pandas as pd

# suma de ratings de cada poi
ny_rating = {} # id_poi: rating_total
tk_rating = {}

recomended_ny = {}
recomended_tk = {}

# pois que ha visitado el usuario
# visits = {} # id_user: [id_po1, id_poi2, ...]

# pois que ha visitado el usuario
pois = []
count = 0

user_in = input("Usuario: ")

# Recorremos los 2 ficheros añadiendo a pois los pois que ya ha visitado el usuario
with open('../train_test/US_NewYork/US_NewYork_train.txt') as ny_train:
    for line_ny in ny_train:
        split_ny = line_ny.split("\t")
        # 0: user
        # 1: poi
        # 2: timestamp
        # 3: rating
        
        # si coincide el usuario, añadimos el poi
        if user_in == split_ny[0]:
            pois.append(split_ny[1])

with open('../train_test/JP_Tokyo/JP_Tokyo_train.txt') as tk_train:
    for line_tk in tk_train:
        split_tk = line_tk.split("\t")
        # 0: user
        # 1: poi
        # 2: timestamp
        # 3: rating

        # si coincide el usuario, añadimos el poi
        if user_in == split_tk[0]:
            pois.append(split_tk[1])

# volvemos a recorrer los ficheros guardando en el diccionario la suma de los 
# ratings de cada poi
with open('../train_test/US_NewYork/US_NewYork_train.txt') as ny_train:
    for line_ny in ny_train:
        split_ny = line_ny.split("\t")
        # 0: user
        # 1: poi
        # 2: timestamp
        # 3: rating

        # visits[split_ny[0]].append(split_ny[1])

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

        # visits[split_tk[0]].append(split_tk[1])

        # si hemos visitado el poi, sumamos el rating que hay con el nuevo
        if split_tk[1] in tk_rating.keys():
            tk_rating[split_tk[1]] = int(tk_rating[split_tk[1]]) + int(split_tk[3].strip())
        # si no lo hemos visitado lo guardamos
        else:
            tk_rating[split_tk[1]] = int(split_tk[3].strip())

# ordenamos los diccionarios de mayor a menor según su rating
sorted_ny = sorted(ny_rating.items(), key=lambda x: x[1], reverse=True)
sorted_tk = sorted(tk_rating.items(), key=lambda x: x[1], reverse=True)


for poi in sorted_ny:
    if poi not in pois:
        count += 1
        recomended_ny[poi[0]] = poi[1]

    if count == 50:
        count = 0
        break
   
for poi in sorted_tk:
    if poi not in pois:
        count += 1
        recomended_tk[poi[0]] = poi[1]

    if count == 50:
        count = 0
        break
   

# if in_city == 'New York':
#     for poi in ny_rating:
#         if poi not in visits[in_user]:
#             cities.append()


