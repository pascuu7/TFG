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
import random

x = [1,2,3,4,5,6,7,8]

random.shuffle(x)

print(x)
