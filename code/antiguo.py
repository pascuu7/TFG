from geopy.distance import distance
from matplotlib.pyplot import cla

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

    cities = {}
    with open("dataset/cities.txt") as fcities:
        for line_city in fcities:
            split_city = line_city.split("\t")
            # creamos el fichero
            open("city_files/" + str(split_city[3]) + "_" + str(split_city[0].replace(" ", "")) + ".txt", "w")
            # añadimos los datos de la ciudad en la lista
            if str(split_city[3]) in cities.keys():
                cities[str(split_city[3])].append((split_city[0], split_city[1], split_city[2]))
            else:
                cities[str(split_city[3])] = [(split_city[0], split_city[1], split_city[2])]

    # for clave in cities:
    #     print(str(clave) + str(cities[clave]) + "\n")
            # cities.append({'nombre': split_city[0], 'coorx': split_city[0], 'coory': split_city[2], 'pais': split_city[3]})

    # ya tengo en cities guardados todos los paises de la siguiente forma (ej):
    #   CR : [('Alajuela', '10.016001', '-84.221000'), ('Heredia', '9.991998', '-84.120003'), ('San Jose', '9.930474', '-84.078621'), ('Cartago', '9.856998', '-83.921004')]
    #   PA : [('Panama', '9.002880', '-79.517079')]


    i = 0
    # ciudad = "HOLA"
    # segundo = "ADIOS"

    # x = {str(ciudad): 3, str(segundo): "SISISISI"}

    with open("dataset/POIs.txt") as fpois:
        for line_poi in fpois:
            min_dist = 6371 # distancia maxima posible en la tierra
            split_poi = line_poi.split("\t")

            for clave in cities.keys():
                if clave == split_poi[4].strip():
                    for city in cities[clave]:
                        # print(city[1] + city[2])
                        dist = distance((city[1], city[2]), (split_poi[1], split_poi[2])).km
                        # print(str(i) + "\t" + str(clave) + " " + str(split_poi[4].strip()))
                        if dist < min_dist:
                            min_dist = dist
                            ciudad = city[0]
                    i += 1
                    
            print(str(i) + '\t' + str(ciudad) + ': ' + str(min_dist) + 'km')
            # print(str(i) + " city_files/" + str(split_poi[4].strip()) + "_" + str(ciudad.replace(" ", "")) + ".txt")
            with open("city_files/" + str(split_poi[4].strip()) + "_" + str(ciudad.replace(" ", "")) + ".txt", "a") as fcities:
                fcities.write(str(int(split_poi[0], 16)) + "\t" + str(split_poi[1]) + "\t" + str(split_poi[2]) + "\t" + str(split_poi[3]) + "\t" + ciudad + "\n")
                    
# int(s,16)
            # for city in cities:
            #     if city['pais'].strip() == split_poi[4].strip():
            #         # funcion distancia
            #         dist = distance((city['coorx'], city['coory']), (split_poi[1], split_poi[2])).km
            #         # calcular minima
            #         if dist < min_dist:
            #             min_dist = dist
            #             ciudad = city['nombre'] # ciudad de menor distancia

            # solo para el print

            # print(str(i) + '\t' + str(ciudad) + ': ' + str(min_dist) + 'km')

    # print(x)

            
            