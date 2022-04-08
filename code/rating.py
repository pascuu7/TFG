import os


contenido = os.listdir('city_checkins/')

dic_timestamp = {}
dic_rating = {}
i = 0

for name in contenido:
    file = 'city_checkins/' + name
    
    with open(file) as fcheck:
        for line_check in fcheck:
            i +=  1
            split_check = line_check.split("\t")
            # 0: user
            # 1: poi
            # 2: timestamp

            # print(i, split_check)

            if split_check[0] not in dic_timestamp.keys():
                dic_timestamp[split_check[0]] = {split_check[1]: split_check[2].strip()}
            else:
                dic_timestamp[split_check[0]][split_check[1]] = split_check[2].strip()

            key = split_check[0] + 'n' + split_check[1] + 'n' + name

            if key not in dic_rating.keys():
                dic_rating[key] = 1
            else:
                dic_rating[key] = dic_rating[key] + 1
                prueba = key
            

open('ratings/JP_Tokyo.txt', 'w')
open('ratings/US_NewYork.txt', 'w')

for key in dic_rating:
    split_rat = key.split('n')

    name = 'ratings/' + split_rat[2].strip()

    file = open(name, 'a')
    file.write(str(split_rat[0]) + '\t' + str(split_rat[1]) + '\t' + str(dic_timestamp[split_rat[0]][split_rat[1]]) + '\t' + str(dic_rating[key]) + '\n')
    # print(split_rat[0], split_rat[1], dic_timestamp[split_rat[0]][split_rat[1]], dic_rating[key])


            # if split_check[0] not in dic.keys():
            #     dic[split_check[0]] = {split_check[1]: (0, split_check[2])}
            # else:
            #     dic[split_check[0]][split_check[1]] = (dic[split_check[0]][split_check[1]][0] + 1, split_check[2])

        




            