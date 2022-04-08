import math

# función para calcular la distancia entre dos coordenadas en km
def haversine(lat1, lon1, lat2, lon2):
    rad=math.pi/180
    dlat=lat2-lat1
    dlon=lon2-lon1
    R=6372.795477598
    a=(math.sin(rad*dlat/2))**2 + math.cos(rad*lat1)*math.cos(rad*lat2)*(math.sin(rad*dlon/2))**2
    distancia=2*R*math.asin(math.sqrt(a))
    return distancia

city_pois = open('POI_city.txt', 'w') # fichero a escribir

cities = {} # diccionarios con pois de cada país
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

j = 0

with open("dataset/POIs.txt") as fpois:
    for line_poi in fpois:
        min_dist = 6371 # distancia maxima posible en la tierra

        split_poi = line_poi.split("\t")
        # 0: id foursquare
        # 1: latitud
        # 2: longitud
        # 3: tipo poi (no lo usamos)
        # 4: codigo país 

        # para reducir el tiempo vemos solo los que sean de US o JP ya que son con los 
        # que vamos a trabajar
        if split_poi[4].strip() == 'US' or split_poi[4].strip() == 'JP' :
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
            if ciudad == 'New York' or ciudad == 'Tokyo':
                j += 1

                # POI_city.txt:
                    # id_nuestro    id_foursquare  latitud  longitud    ciudad
                city_pois.write(str(j) + '\t' + str(split_poi[0]) + '\t' + str(split_poi[1]) + '\t' + str(split_poi[2]) + '\t' + str(split_poi[4].strip()) + "_" + str(ciudad.replace(" ", "")) + '\n')    
            