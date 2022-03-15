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

city_pois = open('POI_city.txt', 'w')

cities = {}
with open("dataset/cities.txt") as fcities:
    for line_city in fcities:
        split_city = line_city.split("\t")
        
        # añadimos los datos de la ciudad en la lista
        if str(split_city[3]) in cities.keys():
            cities[str(split_city[3])].append((split_city[0], split_city[1], split_city[2]))
        else:
            cities[str(split_city[3])] = [(split_city[0], split_city[1], split_city[2])]

# ya tengo en cities guardados todos los paises de la siguiente forma (ej):
#   CR : [('Alajuela', '10.016001', '-84.221000'), ('Heredia', '9.991998', '-84.120003'), ('San Jose', '9.930474', '-84.078621'), ('Cartago', '9.856998', '-83.921004')]
#   PA : [('Panama', '9.002880', '-79.517079')]


i = 0

with open("dataset/POIs.txt") as fpois:
    for line_poi in fpois:
        min_dist = 6371 # distancia maxima posible en la tierra
        split_poi = line_poi.split("\t")

        for clave in cities.keys():
            if clave == split_poi[4].strip():
                for city in cities[clave]:
                    dist = distance((city[1], city[2]), (split_poi[1], split_poi[2])).km
                    if dist < min_dist:
                        min_dist = dist
                        ciudad = city[0]
                i += 1
        
        city_pois.write(str(i) + '\t' + str(split_poi[0]) + '\t' + str(split_poi[4].strip()) + "_" + str(ciudad.replace(" ", "")) + '\n')
        
        print(str(i) + '\t' + str(split_poi[0]) + '\t' + str(split_poi[4].strip()) + "_" + str(ciudad.replace(" ", "")))
        

            
            