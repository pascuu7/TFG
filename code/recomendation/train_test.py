import pandas as pd
import os
from sklearn.model_selection import train_test_split

contenido = os.listdir('../dataset/user_ratings/')

for name in contenido:
    fichero = '../dataset/user_ratings/' + name 
    ciudad = name.replace('.txt', '')
    
    datos = pd.read_csv(fichero, sep='\t', header=None)

    df = pd.DataFrame(datos)


    train, test = train_test_split(df, test_size=0.2)

    ftrain = 'train_test/' + ciudad + '/' + ciudad + '_train.txt'
    ftest = 'train_test/' + ciudad + '/' + ciudad + '_test.txt'

    # US_NewYork_(train/test).txt:
        # id_usuario    id_poi_nuestro  timestamp rating
    train.to_csv(ftrain, sep='\t', index=False, header=None)
    test.to_csv(ftest, sep='\t', index=False, header=None)


