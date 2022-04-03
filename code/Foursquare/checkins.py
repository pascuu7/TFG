import datetime
import os

poi_dic = {}

# id_foursquare: diudad id_nuestro

with open('POI_city.txt') as fpois:
    for line_pois in fpois:
        split_pois = line_pois.split("\t")
        # 0: id nuestro
        # 1: id foursquare
        # 2: latitud
        # 3: longitud
        # 4: ciudad

        poi_dic[str(split_pois[1])] = split_pois[4].strip() + '\t' + split_pois[0]

with open('dataset/checkins.txt') as fcheck:
    for line_check in fcheck:
        split_check = line_check.split("\t")
        # 0: id usuario
        # 1: id poi foursquare
        # 2: fecha
        # 3: offset

        # Hacemos un try except ya que hay algunos checkins con un formato incorrecto
        try:
            split_time = split_check[2].split(" ")

            # Para parsearla después, guardamos la fecha en formato:
            # "03/Apr/2012 18:00:06"
            s_datetime = split_time[2] + '/' + split_time[1] + '/' + split_time[5] + ' ' + split_time[3]
            
            # Parseamos la fecha a formato timestamp para poder tarabajar con él mejor
            tiempo = int(datetime.datetime.strptime(s_datetime, '%d/%b/%Y %H:%M:%S').strftime("%s")) + 7200 
            # En el caso de querer hallar la hora local, se haría lo siguiente:
            # - 60*int(split_check[3]) offset

            # Guardamos en id el id que le hemos asigando nosotros y en fichero el nombre del ficero a crear
            city_id = poi_dic[split_check[1]].split("\t")
            id = city_id[1]
            fichero = "city_checkins/" + city_id[0] + ".txt"

            # US_NewYork.txt:
                # id_usuario    id_poi_nuestro  timestamp
            if os.path.exists(fichero):
                with open(fichero, "a") as fcities:
                    fcities.write(str(split_check[0]) + '\t' + id + '\t' + str(tiempo) + '\n')

            else:
                with open(fichero, "w") as fcities:
                    fcities.write(str(split_check[0]) + '\t' + id + '\t' + str(tiempo) + '\n')
            
        # Si el formato no es correcto saltamos de linea
        except:
            pass
        