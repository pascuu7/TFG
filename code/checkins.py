import datetime
import os

i = 0


with open('dataset/checkins.txt') as fcheck:
    with open('city_pois') as fpois:
        for line_check in fcheck:
            # print(line_check)
            split_check = line_check.split("\t")
            split_time = split_check[2].split(" ")
            s_datetime = split_time[2] + '/' + split_time[1] + '/' + split_time[5] + ' ' + split_time[3]
                        # "03/04/2012 18:00:06"

            time = int(datetime.datetime.strptime(s_datetime, '%d/%b/%Y %H:%M:%S').strftime("%s")) - 60*int(split_check[3])

            # print(str(s_datetime) + '\t' + str(time))
            print(str(split_check[1]))
            for line_pois in fpois:
                # print(line_pois)
                split_pois = line_pois.split("\t")
                print(str(split_pois[1]) + '\t' + str(split_check[1]))
                if split_pois[1] == split_check[1]:
                    # print("HOLAAAA")
                    break
                    # with open("city_checkins/" + str(line_pois[2]) + ".txt", "a") as fcities:
                    #     fcities.write(str(split_check[0]) + '\t' + str(split_check[1]) + '\t' + str(time) + '\n')
                   
                   
                   
                   
                    # print(i)
                    # i += 1
            # print(str(i) + '\t' +  str(split_check))
            # i += 1