""" Se encarga de unir los checkins de ambas aplicaciones (Foursquare y Gowalla)
a través de dos fichero creados anteriormente cuyo contenido muestra las 
correspondencias entre los usuarios y los pois """

import os

# guardamos en contenido la lista de los ficheros de checkins de Gowalla
contenido = os.listdir('Gowalla/city_checkins/')

# diccionarios con los ids correspondientes de Gowalla para pois y users
pois = {} # id_Gowalla: id_Foursquare (a asignar)
users = {} # id_Gowalla: id_correspondiente (a asignar)

# recorremos el fichero de coincidencias de pois y guardamos sus valores en el diccionario 
# correspondiente
with open('coincidencias/coincidencias_pois.txt') as fcoin:
    for line_coin in fcoin:
        split_coin = line_coin.split("\t")
        # 0: id Gowalla
        # 1: id a asignar

        pois[split_coin[0]] = split_coin[1].strip()

# recorremos el fichero de coincidencias de users y guardamos sus valores en el diccionario 
# correspondiente
with open('coincidencias/coincidencias_users.txt') as fusers:
    for line_users in fusers:
        split_users = line_users.split("\t")
        # 0: id Gowalla
        # 1: id a asignar

        users[split_users[0]] = split_users[1].strip()

# recorremos los ficheros de checkins para convertir sus datos (pois y users) a los correspondientes
for name in contenido:
    check_gow_file = 'Gowalla/city_checkins/' + name
    file = 'city_checkins/' + name
    
    with open(check_gow_file) as check_gow:
        for line_gow in check_gow:
            split_check = line_gow.split("\t")
            # 0: id usuario
            # 1: id poi
            # 2: timestamp
            
            # comprobamos si el punto de interes tiene una coincidencia con Foursquare
            if split_check[1] in pois.keys():

                # US_NewYork.txt:
                    # id_usuario    id_poi_nuestro  timestamp
                with open(file, "a") as fcheck:
                    fcheck.write(str(users[split_check[0]]) + '\t' + str(pois[split_check[1]]) + '\t' + str(split_check[2]).strip() + '\n')
                

        

            