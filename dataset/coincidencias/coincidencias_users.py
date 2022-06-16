""" Se encarga de crear la correspondencia de los id de los usuarios de Gowalla
con respecto al id de usuario que le hemos asignado nosotros siguiendo los id de
usuarios de Foursquare """

import os

# guardamos en contenido la lista de ficheros con los checkins de Foursquare
contenido = os.listdir('../Foursquare/city_checkins/')

# listas con los id de los usuarios de Foursquare y Gowalla
four_users = []
gow_users = []

# recorremos los fichero de checkins de Foursquare para hacer una lista de los usuarios
for name in contenido:
    check_four_file = '../Foursquare/city_checkins/' + name

    with open(check_four_file) as check_four:
        for line_four in check_four:
            split_check = line_four.split("\t")
            # 0: id usuario
            # 1: id poi
            # 2: timestamp

            # añadimos el usuario a la lista
            four_users.append(int(split_check[0]))

# cogemos el valor más alto de usuario para continuar con el siguiente en Gowalla
max_user = max(four_users)

# recorremos los ficheros de checkins de Gowalla
for name in contenido:
    check_gow_file = '../Gowalla/city_checkins/' + name
    with open(check_gow_file) as check_gow:
        for line_gow in check_gow:
            split_check = line_gow.split("\t")
            # 0: id usuario
            # 1: id poi
            # 2: timestamp

            # si no está todavía en la lista de usuarios visitados, lo añadimos y lo visitamos
            if split_check[0] not in gow_users:
                gow_users.append(split_check[0])
                # incrementamos en 1 el id a asignar
                max_user += 1

                # coincidencias_users.txt:
                # id_Gowalla    id_asignado
                if os.path.exists('coincidencias_users.txt'):
                    with open('coincidencias_users.txt', "a") as users:
                        users.write(str(split_check[0]) + '\t' + str(max_user) + '\n')

                else:
                    with open('coincidencias_users.txt', "w") as users:
                        users.write(str(split_check[0]) + '\t' + str(max_user) + '\n')
