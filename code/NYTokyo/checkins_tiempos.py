import math
import os
import time

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

coincidenGow = []
coincidenFour = []
users = []

i = 0
j = 0

for name in contenido:
    check_gow_file = 'Gowalla/city_checkins/' + name
    
    with open(check_gow_file) as check_gow:
        for line_gow in check_gow:
            split_gow = line_gow.split("\t")
            users.append(split_gow[0])
            # print(split_gow[0])

for name in contenido:
    check_gow_file = 'Gowalla/city_checkins/' + name
    city = name.replace(".txt", "")

    j += 1

    print(city)
    

    with open('Gowalla/POI_city.txt') as poi_gow:
        for line_poi in poi_gow:
            split_poi = line_poi.split("\t")

            if split_poi[3].strip() == city:
                gow_poi[str(split_poi[0])] = split_poi[1] + '\t' + split_poi[2]


    inicio = time.time()        
    with open('Foursquare/POI_city.txt') as poi_four:
        
        for line_four in poi_four:
            split_four = line_four.split("\t")
        

            # if split_four[4].strip() == city:
            #     if split_four[0] not in coincidenFour:
            #         pass

    fin = time.time()
    print(fin-inicio) 


    inicio = time.time()
    with open(check_gow_file) as check_gow:
        for line_gow in check_gow:
            split_gow = line_gow.split("\t")
            if split_gow[1] not in coincidenGow:

                split_coord = gow_poi[split_gow[1]].split("\t")
                dist = haversine(float(split_four[2]), float(split_four[3]), float(split_coord[0]), float(split_coord[1]))

                # if dist < 5:
                #     coincidenFour.append(1)
                #     coincidenGow.append(1)

            # print(i)
                                
            i += 1  
# 
    fin = time.time()
    print(fin-inicio) 
            


#             print(str(i) + '\t' + str(split_four)) 

        

            