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

poi_dic = {}

i = 0
j = 0

for name in contenido:
    check_gow = 'Gowalla/city_checkins/' + name
    poi_gow = 'Foursquare/city_checkins/' + name
    city = name.replace(".txt", "")

    j += 1

    with open('Gowalla/POI_city.txt') as poi_gow:
        for line_poi in poi_gow:
            split_poi = line_poi.split("\t")

            # print(str(i) + '\t' + str(split_poi[3].strip()) + '\t' + str(city))

            if split_poi[3].strip() == city:
                poi_dic[str(split_poi[0])] = split_poi[1] + '\t' + split_poi[2]

            # print(str(i) + '\t' + str(split_poi) + '\t' + str(city))

            i += 1
        # print(str(j) + '\t' + str(i) + '\t' + str(poi_dic['768067']))


    with open(check_gow) as check_gow:
        for line_check in check_gow:
            split_check = line_check.split("\t")

            coord = poi_dic[split_check[1]]

            print(str(split_check[1]) + '\t' + str(coord)) 

        

            