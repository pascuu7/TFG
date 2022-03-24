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

gow_poi = {} # id: lat\tlong
four_poi = {} # id: lat\tlong

i = 0
j = 0

for name in contenido:
    check_gow = 'Gowalla/city_checkins/' + name
    city = name.replace(".txt", "")

    j += 1

    with open('Gowalla/POI_city.txt') as poi_gow:
        for line_poi in poi_gow:
            split_poi = line_poi.split("\t")

            # print(str(i) + '\t' + str(split_poi[3].strip()) + '\t' + str(city))

            if split_poi[3].strip() == city:
                gow_poi[str(split_poi[0])] = split_poi[1] + '\t' + split_poi[2]

            # print(str(i) + '\t' + str(split_poi) + '\t' + str(city))

        # print(str(j) + '\t' + str(i) + '\t' + str(poi_dic['768067']))


            
    with open('Foursquare/POI_city.txt') as poi_four:
        for line_four in poi_four:
            split_four = line_four.split("\t")

            # print(str(split_four[4].strip()) + '\t' + str(city))

            if split_four[4].strip() == city:

                with open(check_gow) as check_gow:
                    for line_gow in check_gow:
                        split_gow = line_gow.split("\t")

                        split_coord = gow_poi[split_gow[1]].split("\t")

                        # print(str(split_coord[0]) + '\t' + str(split_coord[1]))
            i += 1
                
                # dist = haversine(float(split_four[2]), float(split_four[3]), float(split_coord[0]), float(split_coord[1]))
                        


            print(str(i) + '\t' + str(split_four)) 

        

            