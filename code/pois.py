import os
files = os.listdir('cities_pois/')
i = 0

# fpois = open('city_poi', 'w')
fpois = open('city_pois', 'w')
for file in files:
    city = file.replace('.txt', '')
    with open('cities_pois/' + str(file)) as fcities:
        for line_cities in fcities:
            split_cities = line_cities.split("\t")
            # fpois.write(str(i) + '\t' + city + '\n')
            # print(str(num) + '\t' + str(split_cities[0]))
            # print(str(hex(int(split_cities[0]))) + '\t' + str(split_cities[0]) + '\t' + str(split_cities[4]))
            # print(str(i) + '\t' + str(hex(int(split_cities[0]))).replace('0x', ''))
            fpois.write(str(i) + '\t' + str(hex(int(split_cities[0]))).replace('0x', '') + '\t' + city + '\n')
            print(i)
            i += 1

# print(str(hex(int())).replace('0x', ''))