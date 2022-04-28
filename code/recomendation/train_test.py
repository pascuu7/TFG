""" Se encarga de crear los ficheros correspondientes, dividiendo aleatoriamente los 
los datos entre train y test """

import pandas as pd
import os
from sklearn.model_selection import train_test_split

# listado de ficheros de ratings de Foursquare
contenido = os.listdir('../dataset/Foursquare/user_ratings/')

# recorremos cada fichero
for name in contenido:
    fichero = '../dataset/Foursquare/user_ratings/' + name 
    # guardamos el nomnbre de la ciudad que estamos visitando
    ciudad = name.replace('.txt', '')
    
    # para leer el fichero usamos pandas
    datos = pd.read_csv(fichero, sep='\t', header=None)
    df = pd.DataFrame(datos)

    # separamos entre train y test siendo test un 20%
    train, test = train_test_split(df, test_size=0.2)

    # nombre de los nuevos ficheros
    ftrain = 'train_test/' + ciudad + '/' + ciudad + '_train.txt'
    ftest = 'train_test/' + ciudad + '/' + ciudad + '_test.txt'

    # US_NewYork_(train/test).txt:
        # id_usuario    id_poi_nuestro  timestamp rating
    train.to_csv(ftrain, sep='\t', index=False, header=None)
    test.to_csv(ftest, sep='\t', index=False, header=None)


