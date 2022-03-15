import datetime
import math
import os

def haversine(lat1, lon1, lat2, lon2):
    rad=math.pi/180
    dlat=lat2-lat1
    dlon=lon2-lon1
    R=6372.795477598
    a=(math.sin(rad*dlat/2))**2 + math.cos(rad*lat1)*math.cos(rad*lat2)*(math.sin(rad*dlon/2))**2
    distancia=2*R*math.asin(math.sqrt(a))
    return distancia

i = 0
contenido = os.listdir('../eight_cities')

with open('city_coordinates.txt') as fcoor:
    for line_coord in fcoor:
        split_coor = line_coord.split("\t")

        with open('Gowalla_totalCheckins.txt') as fcheck:
            for line_check in fcheck:
                split_check = line_check.split("\t")
                i += 1 
                dist = haversine(float(split_check[2]), float(split_check[3]),float(split_coor[1]), float(split_coor[2]))
                if dist < 30:    

                    time = split_check[1].split('T')
                    s_datetime = time[0] + ' ' + time[1][:-1]

                    tiempo = int(datetime.datetime.strptime(s_datetime, '%Y-%m-%d %H:%M:%S').strftime("%s")) + 7200

                    for name in contenido:
                        if split_coor[0].replace(" ", "") in name:
                            fichero = "city_checkins/" + name

                            if os.path.exists(fichero):
                                with open(fichero, "a") as fcities:
                                    fcities.write(str(split_check[0]) + '\t' + str(split_check[4]).strip() + '\t' + str(tiempo) + '\n')

                            else:
                                with open(fichero, "w") as fcities:
                                    fcities.write(str(split_check[0]) + '\t' + str(split_check[4]).strip() + '\t' + str(tiempo) + '\n')







