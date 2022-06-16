""" Se encarga de crear el fichero con todos los puntos de interés, viendo antes
a que ciudad pertenece usando la función haversine """

import sys

sys.path.append('../../')

from functions import haversine

city_pois = open('POI_city.txt', 'w')  # fichero a escribir

# diccionarios con pois de cada país
cities = {}  # codigo_pais: (ciudad1, latitud1, longitud1), (ciudad2, latitud2, longitud2)...

with open("dataset/cities.txt") as fcities:
    for line_city in fcities:
        split_city = line_city.split("\t")
        # 0: nombre ciudad
        # 1: latitud
        # 2: longitud
        # 3: codigo pais
        # 4: nombre pais (no lo usamos)
        # 5: tipo de ciudad (no lo usamos)

        # añadimos los datos de la ciudad en la lista
        if str(split_city[3]) in cities.keys():
            cities[str(split_city[3])].append((split_city[0], split_city[1], split_city[2]))
        else:
            cities[str(split_city[3])] = [(split_city[0], split_city[1], split_city[2])]

# ya estan en cities guardados todos los paises de la siguiente forma (ej):
#   CR : [('Alajuela', '10.016001', '-84.221000'), ('Heredia', '9.991998', '-84.120003'), ('San Jose', '9.930474', '-84.078621'), ('Cartago', '9.856998', '-83.921004')]
#   PA : [('Panama', '9.002880', '-79.517079')]

# id de los pois
i = 0
with open("dataset/POIs.txt") as fpois:
    for line_poi in fpois:
        min_dist = 6371  # distancia maxima posible en la tierra

        split_poi = line_poi.split("\t")
        # 0: id foursquare
        # 1: latitud
        # 2: longitud
        # 3: tipo poi (no lo usamos)
        # 4: codigo país

        # para reducir el tiempo vemos solo los que sean de US o JP ya que son con los
        # que vamos a trabajar
        if split_poi[4].strip() == 'US' or split_poi[4].strip() == 'JP':
            for clave in cities.keys():
                if clave == split_poi[4].strip():
                    # recorremos los pois del país
                    for city in cities[clave]:
                        dist = haversine(float(city[1]), float(city[2]), float(split_poi[1]), float(split_poi[2]))
                        if dist < min_dist:
                            min_dist = dist
                            # guardamos la ciudad a la que pertenece si es menor que la distancia
                            # minima anterior
                            ciudad = city[0]

            # para reducir el tiempo, cremos únicamente el fichero de pois con los pois de las
            # ciudades con las que vamos a trabajar
            if ciudad == 'New York' or ciudad == 'Tokyo' or ciudad == 'San Francisco':
                # incrementamos en 1 el id del poi
                i += 1

                # POI_city.txt:
                # id_nuestro    id_foursquare  latitud  longitud    ciudad
                city_pois.write(str(i) + '\t' + str(split_poi[0]) + '\t' + str(split_poi[1]) + '\t' + str(split_poi[2]) + '\t' + str(split_poi[4].strip()) + "_" + str(ciudad.replace(" ", "")) + '\n')
