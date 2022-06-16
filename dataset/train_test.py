""" Se encarga de crear los ficheros correspondientes, dividiendo aleatoriamente los
los datos entre train y test """

import pandas as pd
import os
from sklearn.model_selection import train_test_split

# listado de ficheros de ratings de Foursquare
contenido = os.listdir('Foursquare/user_ratings/')

# recorremos cada fichero
for name in contenido:
    fichero = 'Foursquare/user_ratings/' + name
    # guardamos el nomnbre de la ciudad que estamos visitando
    ciudad = name.replace('.txt', '')

    # para leer el fichero usamos pandas
    datos = pd.read_csv(fichero, sep='\t', header=None)
    df = pd.DataFrame(datos)

    # separamos entre train y test siendo test un 20%
    train, test = train_test_split(df, test_size=0.2)

    # nombre de los nuevos ficheros de Foursquare
    ftrain = '../recomendation/train_test/Gowalla/' + ciudad + '/' + ciudad + '_train.txt'
    ftest = '../recomendation/train_test/Gowalla/' + ciudad + '/' + ciudad + '_test.txt'

    # US_NewYork_(train/test).txt:
    # id_usuario    id_poi_nuestro  timestamp rating
    train.to_csv(ftrain, sep='\t', index=False, header=None)
    test.to_csv(ftest, sep='\t', index=False, header=None)

    # nombre de los nuevos ficheros de Foursquare + Gowalla
    ftrain = '../recomendation/train_test/Foursquare/' + ciudad + '/' + ciudad + '_train.txt'
    ftest = '../recomendation/train_test/Foursquare/' + ciudad + '/' + ciudad + '_test.txt'

    train.to_csv(ftrain, sep='\t', index=False, header=None)
    test.to_csv(ftest, sep='\t', index=False, header=None)

# pasamos a añadir los ratings de Gowalla en train
users = set()
contenido = os.listdir('../recomendation/train_test/Gowalla/')

# recorremos cada fichero
for name in contenido:
    fratings = 'user_ratings/' + name + '.txt'

    with open(ftrain) as train:
        for line in train:
            split = line.split("\t")
            # 0: user
            # 1: poi
            # 2: timestamp
            # 3: rating

            users.add(int(split[0]))

    with open(ftest) as test:
        for line in test:
            split = line.split("\t")
            # 0: user
            # 1: poi
            # 2: timestamp
            # 3: rating

            users.add(int(split[0]))

    maximo = max(users)
    out = '../recomendation/train_test/Gowalla/' + name + '/' + name + '_train.txt'

    fout = open(out, "a")
    with open(fratings) as ratings:
        for line in ratings:
            split = line.split("\t")
            # 0: user
            # 1: poi
            # 2: timestamp
            # 3: rating

            if int(split[0]) > maximo:
                fout.write(line)
