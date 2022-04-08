import math
import os

# utilizamos la funcion haversine para calcular la distancia entre dos coordenadas
# aunque en esta multiplicamos por 1000n ya que la vamos a utilizar en metros

def haversine(lat1, lon1, lat2, lon2):
    rad=math.pi/180
    dlat=lat2-lat1
    dlon=lon2-lon1
    R=6372.795477598
    a=(math.sin(rad*dlat/2))**2 + math.cos(rad*lat1)*math.cos(rad*lat2)*(math.sin(rad*dlon/2))**2
    distancia=2*R*math.asin(math.sqrt(a))
    return distancia*1000

# guardamos en contenido la lista de ficheros con los checkins de Gowalla
contenido = os.listdir('../Gowalla/city_checkins/')

# guardamos en un diccionarios pois correspondientes a cada ciudad con sus respectivas coordenadas
poi_ny = {} # id: lat\tlong
poi_tokyo = {} # id: lat\tlong

# recorremos el fichero de los pois de Foursquare guardandolos en el diccionario correspondiente 
with open('../Foursquare/POI_city.txt') as poi_four:
    for line_poi in poi_four:
        split_poi = line_poi.split("\t")
        # 0: id nuestro
        # 1: id foursquare
        # 2: latitud
        # 3: longitud
        # 4: ciudad 

        if split_poi[4].strip() == "US_NewYork":
            poi_ny[str(split_poi[0])] = (split_poi[2], split_poi[3])

        else:
            poi_tokyo[str(split_poi[0])] = (split_poi[2], split_poi[3])


# recorremos el fichero de pois de Gowalla para ver las correspondencias
with open('../Gowalla/POI_city.txt') as poi_gow:
    for line_poi in poi_gow:
        split_poi = line_poi.split("\t")
        # 0: id nuestro
        # 1: latitud
        # 2: longitud
        # 3: ciudad

        # distancia minima para que coincidan los pois
        min_dist = 5

        # comprobamos a que ciudad pertenece el poi para utilizar el diccionario correspondiente
        if split_poi[3].strip() == 'US_NewYork':
            for key in poi_ny:
                # calculamos la distancia entre los pois
                dist = haversine(float(poi_ny[key][0]), float(poi_ny[key][1]), float(split_poi[1]), float(split_poi[2]))
                # si es menor de 5 metros y menor que la distacia anterior, guarda los ids en coincidencias. Habrá
                # repetidos en coincidencias_pois pero como luego se irán añadiendo en un diccionario, solo se
                # guardará la ultima coincidencia vista, es decir, la de menor distancia
                if dist < 5 and dist < min_dist:
                    # se actualiza la distancia minima
                    min_dist = dist

                    # coincidencias_pois.txt:
                    # id_Gowalla    id_Foursquare
                    if os.path.exists("coincidencias_pois.txt"):
                        with open("coincidencias_pois.txt", "a") as fcoin:
                            fcoin.write(str(split_poi[0]) + '\t' + str(key) + '\n')

                    else:
                        with open("coincidencias_pois.txt", "w") as fcoin:
                            fcoin.write(str(split_poi[0]) + '\t' + str(key) + '\n')
          
        # mismo procedimiento para Tokyo
        else:
           for key in poi_tokyo:
                
                dist = haversine(float(poi_tokyo[key][0]), float(poi_tokyo[key][1]), float(split_poi[1]), float(split_poi[2]))
                if dist < 5 and dist < min_dist:
                    min_dist = dist
                    if os.path.exists("coincidencias_pois.txt"):
                        with open("coincidencias_pois.txt", "a") as fcoin:
                            fcoin.write(str(split_poi[0]) + '\t' + str(key) + '\n')
                    else:
                        with open("coincidencias_pois.txt", "w") as fcoin:
                            fcoin.write(str(split_poi[0]) + '\t' + str(key) + '\n')

        