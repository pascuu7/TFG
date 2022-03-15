# import math
# from geopy.distance import distance

# def haversine(lat1, lon1, lat2, lon2):
#     rad=math.pi/180
#     dlat=lat2-lat1
#     dlon=lon2-lon1
#     R=6372.795477598
#     a=(math.sin(rad*dlat/2))**2 + math.cos(rad*lat1)*math.cos(rad*lat2)*(math.sin(rad*dlon/2))**2
#     distancia=2*R*math.asin(math.sqrt(a))
#     return distancia

# import datetime
import os

# poi_dic = {}

# i = 0

# with open('data.txt', 'w') as fprueba:
#     fprueba.write("11222\t4bdaf5a23904a593d805489e\tWed Mar 27 17:40:17 +0000 2013\t120\n17690\t4b82d30cf964a52065e730e3\tWed Mar 27 17:40:18 +0000 2013\t120\n218711\t4b1aad22f964a5201def23e3\tWed Mar 27 17:40:21 +0000 2013\t-30\n135077\t4bc8351d0050b713e9f6b93b\tWed Mar 27 17:429793\t120\n140320\t4d83593202eb5481f15b17f5\tWed Mar 27 17:40:22 +0000 2013\t-180\n130643\t4fe13ceae4b01ac720143695\tWed Mar 27 17:40:23 +0000 2013\t-180\n112187\t4b292e69f964a5207a9a24e3\tWed Mar 27 17:40:24 +0000 2013\t120")
# with open('POI_city.txt') as fpois:
#     for line_pois in fpois:
#         split_pois = line_pois.split("\t")

#         poi_dic[str(split_pois[1])] = split_pois[2].strip() + '\t' + split_pois[0]

# with open('data.txt') as fcheck:
#     for line_check in fcheck:
#         split_check = line_check.split("\t")
#         print(str(i) + '\t' + str(split_check[0]))

#         try:
#             split_time = split_check[2].split(" ")
            
#             s_datetime = split_time[2] + '/' + split_time[1] + '/' + split_time[5] + ' ' + split_time[3]

#             tiempo = int(datetime.datetime.strptime(s_datetime, '%d/%b/%Y %H:%M:%S').strftime("%s")) + 7200 

#             city_id = poi_dic[split_check[1]].split("\t")
#             id = city_id[1]
#             fichero = "city_checkins/" + city_id[0] + ".txt"

#             i += 1


#             if os.path.exists(fichero):
#                 with open(fichero, "a") as fcities:
#                     fcities.write(str(split_check[0]) + '\t' + id + '\t' + str(tiempo) + '\n')


#             else:
#                 with open(fichero, "w") as fcities:
#                     fcities.write(str(split_check[0]) + '\t' + id + '\t' + str(tiempo) + '\n')
#         except:
#             pass
        

# with open('Gowala/city_coordinates.txt') as fcoor:
#     for line_coord in fcoor:
#         print(line_coord.strip())
        
#         split_coor = line_coord.split("\t")
#         print(split_coor)

# x1 = 40.663962
# y1 = -74.011221

# x2 = 40.733596
# y2 = -74.003139

# distancia1 = math.sqrt((x2-x1)**2+(y2-y1)**2)
# distancia2 = dist = distance((x1, y1), (x2, y2)).km
# distancia3 = haversine(x1, y1, x2, y2)

# print(str(distancia1) + '\t' + str(distancia2) + '\t' + str(distancia3))

# original = "2010-07-24T13:45:06Z"
# tiempo = original.split("T")
# dia = tiempo[0]
# hora = tiempo[1][:-1]

# print(str(dia) + '\t' + str(hora))

contenido = os.listdir('.')
print(contenido)