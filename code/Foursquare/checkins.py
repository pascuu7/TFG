import datetime
import os

poi_dic = {}

i = 0

with open('POI_city.txt') as fpois:
    for line_pois in fpois:
        split_pois = line_pois.split("\t")

        poi_dic[str(split_pois[1])] = split_pois[2].strip() + '\t' + split_pois[0]

with open('dataset/checkins.txt') as fcheck:
    for line_check in fcheck:
        split_check = line_check.split("\t")

        try:
            split_time = split_check[2].split(" ")

            s_datetime = split_time[2] + '/' + split_time[1] + '/' + split_time[5] + ' ' + split_time[3]
            # "03/Apr/2012 18:00:06"

            tiempo = int(datetime.datetime.strptime(s_datetime, '%d/%b/%Y %H:%M:%S').strftime("%s")) + 7200 
            # - 60*int(split_check[3]) offset

            city_id = poi_dic[split_check[1]].split("\t")
            id = city_id[1]
            fichero = "city_checkins/" + city_id[0] + ".txt"
 
            i += 1
            print(str(i) + '\t' + str(split_check[0]) + '\t' + id + '\t' + str(tiempo))

            if os.path.exists(fichero):
                with open(fichero, "a") as fcities:
                    fcities.write(str(split_check[0]) + '\t' + id + '\t' + str(tiempo) + '\n')

            else:
                with open(fichero, "w") as fcities:
                    fcities.write(str(split_check[0]) + '\t' + id + '\t' + str(tiempo) + '\n')
            
        except:
            pass
        