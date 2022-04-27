import pandas as pd
from sklearn.model_selection import train_test_split

datos = pd.read_csv("user_ratings/US_NewYork.txt", sep='\t')
df = pd.DataFrame(datos)

train, test = train_test_split(df, random_state = 0)

print(train.shape)
print(test.shape)