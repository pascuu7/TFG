# import pandas as pd
# from sklearn.model_selection import train_test_split

# datos = pd.read_csv('dataset/user_ratings/US_NewYork.txt', sep='\t', header=None)

# df = pd.DataFrame(datos)

# print(df)

# train, test = train_test_split(df, test_size=0.2)

# train.to_csv('train.txt', sep='\t', index=False)

# import operator

# dic = {'C': 1, 'B': 3, 'A': 2}

# new = sorted(dic.items(), key=lambda x: x[1], reverse=True)

# print(new)

# i = 2

# next(i)

# print(i)

# with open('recomendation/train_test/US_NewYork/US_NewYork_train.txt') as file:
#     for line in file:
#         split = line.split("\t")
#         # 0: id user
#         # 1: id poi
#         # 2: timestamp
#         # 3: rating
#         if int(split[1]) == 971:
#             print(split[0])


# l1 = set([1, 5, 3, 4, 2])
# l2 = set([5, 1, 7, 6, 2])
# l3 = set([7, 6, 1, 8, 9])

# pr = set()

# for l in l1:
#     pr.add(l)
# print("Common Elements", pr)
# for l in l2:
#     pr.add(l)
# print("Common Elements", pr)
# for l in l3:
#     pr.add(l)
# print("Common Elements", pr)

# print("Common Elements", pr)
# pr = pr | l1
# print("Common Elements", pr)
# pr = pr | l2
# print("Common Elements", pr)
# pr = pr | l3
# print("Common Elements", pr)

# from functions import read_users

# users = read_users('recomendation/train_test/Foursquare/US_NewYork/US_NewYork_test.txt')

# print(len(users))

import math

def haversine(lat1, lon1, lat2, lon2):
    rad=math.pi/180
    dlat=lat2-lat1
    dlon=lon2-lon1
    R=6372.795477598
    a=(math.sin(rad*dlat/2))**2 + math.cos(rad*lat1)*math.cos(rad*lat2)*(math.sin(rad*dlon/2))**2
    distancia=2*R*math.asin(math.sqrt(a))
    return distancia


print(haversine(37.795815, -122.380092, 34.000002, -118.250001))
print(haversine(37.795815, -122.380092, 41.826546, -87.641298))
print(haversine(41.826546, -87.641298, 34.000002, -118.250001))
