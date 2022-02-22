from geopy.distance import distance

# Cities
#   ciudad nombre = split_city[0]
#   coordenadas = split_city[1] y split_city[2]
#   codigo pais = split_city[3]
#   nombre pais = split_city[4]


# POIS
#   id = split_poi[0]
#   coordenadas = split_poi[1] y split_poi[2]
#   codigo pais = split_poi[4]

if __name__ == "__main__":

    # with open("dataset/POIs.txt") as fpois:
        # with open("dataset/cities.txt") as fcities:
        #     for line_poi in fpois:
        #         split_poi = line_poi.split("\t")
        #         print(str(split_poi[3]) + "\n")
        #         for line_city in fcities:
        #             split_city = line_city.split("\t")
        #             dist = distance((split_city[1], split_city[2]), (split_poi[1], split_poi[2])).km
        #             if dist < min_dist:
        #                 dicc = split_city[3], split_city[0], split_poi[0]
        #             # if distance((split_city[1], split_city[2]), (split_poi[1], split_poi[2])).km < 50:
        #             #     file = open("city_files/" + str(split_city[3]) + "_" + str(split_city[0].replace(" ", "")) + ".txt", "w")
        #             #     file.write(line_poi)

        #         break

    cities = []
    with open("dataset/cities.txt") as fcities:
        for count, line_city in enumerate(fcities):
            split_city = line_city.split("\t")
            # creamos el fichero
            open("city_files/" + str(split_city[3]) + "_" + str(split_city[0].replace(" ", "")) + ".txt", "w")
            # añadimos los datos de la ciudad en la lista
            cities.append({'nombre': split_city[0], 'coorx': split_city[1], 'coory': split_city[2], 'pais': split_city[3]})

    # ya tengo en cities guardados todos los paises de la siguiente forma (ej):
    #   {'nombre': 'Cuiaba', 'coorx': '-15.615000', 'coory': '-56.093004', 'pais': 'BR'}

    i = 0
    with open("dataset/POIs.txt") as fpois:
        for line_poi in fpois:
            min_dist = 6371 # distancia maxima posible en la tierra
            split_poi = line_poi.split("\t")
            for city in cities:
                # funcion distancia
                dist = distance((city['coorx'], city['coory']), (split_poi[1], split_poi[2])).km
                # calcular minima
                if dist < min_dist:
                    min_dist = dist
                    ciudad = city['nombre'] # ciudad de menor distancia

            # solo para el print
            i += 1

            print(str(i) + '\t' + str(ciudad) + ': ' + str(min_dist) + 'km')
            