# ftrain = 'segunda_parte/recomendation/train_test/Foursquare/US_SanFrancisco/US_SanFrancisco_train.txt'
# ftrain2 = 'segunda_parte/recomendation/train_test/Gowalla/US_SanFrancisco/US_SanFrancisco_train.txt'
# num = 0

# # with open(ftrain) as train:
# #         for line in train:
# #             split = line.split("\t")
# #             # 0: user
# #             # 1: poi
# #             # 2: timestamp
# #             # 3: rating

# #             if int(split[1]) == 44521:
# #                 num += 1

# print(len(read_users(ftrain)))
# print(len(read_users(ftrain2)))

# print(num)

# file = '../../tercera_parte/dataset/Gowalla/POI_city.txt'

# users = set()

# with open(file) as test:
#     i = 0
#     for line in test:
#         i += 1
#         print(i)
#         split = line.split("\t")
#         # 0: user
#         # 1: poi
#         # 2: timestamp
#         # 3: rating

#         if split[4].strip() == 'US_SanFrancisco':
#             users.add(int(split[0]))
# print(len(users))

# import os

# contenido = os.listdir('../otros/cities_pois/')

# ciudades = {}

# # recorremos cada fichero
# for name in contenido:
#     nombre = '../otros/cities_pois/' + name 
#     fichero = open(nombre, 'r')
#     print(name, len(fichero.readlines()))
#     fichero.close()
#     # ciudades[name] = len(fichero.readlines())

file = 'recomendation/train_test/Foursquare/JP_Tokyo/JP_Tokyo_test.txt'

users = set()


with open(file) as test:
    i = 0
    for line in test:
        i += 1
        # print(i)
        split = line.split("\t")
        # 0: user
        # 1: poi
        # 2: timestamp
        # 3: rating

        users.add(int(split[0]))

print(len(users))
