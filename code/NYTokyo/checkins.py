# import os

# i = 0

# print("HOLAAAA")

# contenido = os.listdir('Foursquare/city_checkins/')

# four_users = []

# pois = {}

# for name in contenido:
#     check_four_file = 'Foursquare/city_checkins/' + name
#     file = 'city_checkins/' + name
    
#     with open(check_four_file) as check_four:
#         for line_four in check_four:
#             split_check = line_four.split("\t")
#             four_users.append(int(split_check[0]))
#             if os.path.exists(file):
#                 with open(file, "a") as fcheck:
#                     fcheck.write(line_four)

#             else:
#                 with open(file, "w") as fcheck:
#                     fcheck.write(line_four)
#                 pass

# # print(max(users))



# with open('coincidencias.txt') as fcoins:
#     for line_coin in fcoins:
#         split_coins = line_coin.split('\t')
#         pois[split_coins[0]] = split_coins[1]

# print(pois)

        

            