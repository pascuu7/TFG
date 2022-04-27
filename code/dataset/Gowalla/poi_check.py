""" Se encarga de crear el fichero de puntos de interés calculando la distancia
de los pois de Gowalla con respecto a las coordenadas de las ciudades según 
Foursquare. Además crea los respectivos ficheros de checkins para Gowalla habiendo
transformado antes la fecha dada en timestamp (solo nos quedamos con los checkins
de las ciudades que hemos seleccionado) """

import datetime
import math
import os

# funcion haversine para calcular la distancia entre dos coordenadas
def haversine(lat1, lon1, lat2, lon2):
    rad=math.pi/180
    dlat=lat2-lat1
    dlon=lon2-lon1
    R=6372.795477598
    a=(math.sin(rad*dlat/2))**2 + math.cos(rad*lat1)*math.cos(rad*lat2)*(math.sin(rad*dlon/2))**2
    distancia=2*R*math.asin(math.sqrt(a))
    return distancia
    
# guardamos una lista de los txt con los checkins de las ciudades de Foursquare
contenido = os.listdir('../Foursquare/city_checkins/')

poi_city = open('POI_city.txt', 'w')
pois = [] # lista con los pois que ya se han visitado para no duplicar

# coordinates contiene los datos de las ciudades que hemos escogido
with open('city_coordinates.txt') as fcoor:
    for line_coord in fcoor:
        split_coor = line_coord.split("\t")
        # 0: nombre ciudad
        # 1: latitud
        # 2: longitud
        # 3: codigo país
        # 4: nombre país (no lo usamos)
        # 5: tipo de ciudad (no lo usamos)

        with open('Gowalla_totalCheckins.txt') as fcheck:
            for line_check in fcheck:
                split_check = line_check.split("\t")
                # 0: id usuario
                # 1: fecha
                # 2: latitud
                # 3: longitud
                # 4: id poi

                id = split_check[4].strip()

                # calculamos la distancia con la ciudad que estamos visitando en coordinates
                dist = haversine(float(split_check[2]), float(split_check[3]),float(split_coor[1]), float(split_coor[2]))
                
                # usamos una distancia menor que 30km ya que al tener ciudades de diferentes países
                # no se cumple con dos ciudades diferentes
                if dist < 30:    
                    # ya que viene en formato: 2010-07-24T13:45:06Z separamos el día de la hora.
                    time = split_check[1].split('T')

                    # lo pasamos al formato que queremos para poder parsearlo (quitando la Z del final)
                    s_datetime = time[0] + ' ' + time[1][:-1]
                    tiempo = int(datetime.datetime.strptime(s_datetime, '%Y-%m-%d %H:%M:%S').strftime("%s")) + 7200

                    # recorremos todos los ficheros
                    for name in contenido:
                        # si la ciudad correspondiente coincide con el fichero escribimos en el fichero de esa ciudad para los checkins y en el
                        # caso de los pois escribimos el nombre de la ciudad a la que pertenece 
                        if split_coor[0].replace(" ", "") in name:
                            # si no hemos guardado ya ese poi, lo guardamos
                            if id not in pois:
                                pois.append(id)
                                # POIs.txt:
                                    # id_poi    latitud     longitud    ciudad
                                poi_city.write(str(id) + '\t' + str(split_check[2]) + '\t' + str(split_check[3]) + '\t' + str(name).replace('.txt', '') + '\n')

                            fichero = "city_checkins/" + name

                            # US_NewYork.txt:
                                # id_usuario    id_poi  timestamp
                            if os.path.exists(fichero):
                                with open(fichero, "a") as fcities:
                                    fcities.write(str(split_check[0]) + '\t' + str(split_check[4]).strip() + '\t' + str(tiempo) + '\n')

                            else:
                                with open(fichero, "w") as fcities:
                                    fcities.write(str(split_check[0]) + '\t' + str(split_check[4]).strip() + '\t' + str(tiempo) + '\n')
