from genericpath import exists
import pandas as pd

# suma de ratings de cada poi
ny_rating = {} # id_poi: rating_total
tk_rating = {}

# pois que ha visitado el usuario
visits = {} # id_user: [id_po1, id_poi2, ...]

cities = []
i = 0

# in_user = input("Usuario: ")
# in_city = input("City: ")

with open('../train_test/US_NewYork/US_NewYork_train.txt') as ny_train:
    for line_ny in ny_train:
        split_ny = line_ny.split("\t")
        # 0: user
        # 1: poi
        # 2: timestamp
        # 3: rating

        i += 1
        print(i)

        visits[split_ny[0]].append(split_ny[1])

       

        if split_ny[1] in ny_rating.keys():
            ny_rating[split_ny[1]] = int(ny_rating[split_ny[1]]) + int(split_ny[3].strip())
        else:
            ny_rating[split_ny[1]] = int(split_ny[3].strip())

with open('../train_test/JP_Tokyo/JP_Tokyo_train.txt') as tk_train:
    for line_tk in tk_train:
        split_tk = line_tk.split("\t")
        # 0: user
        # 1: poi
        # 2: timestamp
        # 3: rating

        visits[split_tk[0]].append(split_tk[1])

        if split_tk[1] in tk_rating.keys():
            tk_rating[split_tk[1]] = int(tk_rating[split_tk[1]]) + int(split_tk[3].strip())
        else:
            tk_rating[split_tk[1]] = int(split_tk[3].strip())

sorted_ny = sorted(ny_rating.items(), key=lambda x: x[1], reverse=True)

print(sorted_ny)

# if in_city == 'New York':
#     for poi in ny_rating:
#         if poi not in visits[in_user]:
#             cities.append()


sorted_tk = sorted(tk_rating.items(), key=lambda x: x[1], reverse=True)
