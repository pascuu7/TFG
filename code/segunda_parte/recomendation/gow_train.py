import os

users = set()

contenido = os.listdir('train_test/Gowalla/')

# recorremos cada fichero
for name in contenido:
    ftest = 'train_test/Foursquare/' + name + '/' + name + '_test.txt'
    ftrain = 'train_test/Foursquare/' + name  + '/' + name + '_train.txt'

    fratings = '../dataset/user_ratings/' + name + '.txt'

    print('TRAIN')

    with open(ftrain) as train:
        for line in train:
            split = line.split("\t")
            # 0: user
            # 1: poi
            # 2: timestamp
            # 3: rating

            users.add(int(split[0]))

    print('TEST')

    with open(ftest) as test:
        for line in test:
            split = line.split("\t")
            # 0: user
            # 1: poi
            # 2: timestamp
            # 3: rating

            users.add(int(split[0]))

    i = 0
    maximo = max(users)

    print('RATING')

    coin = set()

    out = 'train_test/Gowalla/' + name  + '/' + name + '_train.txt'

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
    

        

                
