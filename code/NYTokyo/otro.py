import time
import math
import os

def haversine(lat1, lon1, lat2, lon2):
    rad=math.pi/180
    dlat=lat2-lat1
    dlon=lon2-lon1
    R=6372.795477598
    a=(math.sin(rad*dlat/2))**2 + math.cos(rad*lat1)*math.cos(rad*lat2)*(math.sin(rad*dlon/2))**2
    distancia=2*R*math.asin(math.sqrt(a))
    return distancia*1000

contenido = os.listdir('Gowalla/city_checkins/')

poi_ny = {} # id: lat\tlong
poi_tokyo = {} # id: lat\tlong
coincidencias = {} # id Gow: id Four

i = 0

with open('Foursquare/POI_city.txt') as poi_four:
    for line_poi in poi_four:
        split_poi = line_poi.split("\t")

        if split_poi[4].strip() == "US_NewYork":
            poi_ny[str(split_poi[0])] = (split_poi[2], split_poi[3])

        else:
            poi_tokyo[str(split_poi[0])] = (split_poi[2], split_poi[3])



with open('Gowalla/POI_city.txt') as poi_gow:
    
    for line_poi in poi_gow:
        split_poi = line_poi.split("\t")

        if split_poi[3].strip() == 'US_NewYork':
            inicio = time.time()
            for key in poi_ny:
                pass
                # print(str(poi_ny[key][0]), str(poi_ny[key][1]), str(split_poi[1]), str(split_poi[2]))
                dist = haversine(float(poi_ny[key][0]), float(poi_ny[key][0]), float(split_poi[1]), float(split_poi[2]))
                if dist < 5:
                    print("ENTRA")
            fin = time.time()
            print(fin-inicio)

         
        else:
            pass
            # inicio = time.time()
            # for key in poi_tokyo:
            #     # print(str(poi_tokyo[key][0]), str(poi_tokyo[key][1]), str(split_poi[1]), str(split_poi[2]))
                
            #     dist = haversine(float(poi_tokyo[key][0]), float(poi_tokyo[key][0]), float(split_poi[1]), float(split_poi[2]))
            #     if dist < 5:
            #         print("ENTRA")

            # fin = time.time()
            # print(fin-inicio)
        i += 1
        print(i)

        