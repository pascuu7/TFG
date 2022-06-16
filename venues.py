from functions import sort_recomendations

def venue(ftrain):
    # suma de ratings de cada poi
    rating = {} # id_poi: rating_total

    # Recorremos el fichero para guardar en el diccionario 
    # la suma de los ratings de cada poi
    with open(ftrain) as train:
        for line in train:
            split = line.split("\t")
            # 0: user
            # 1: poi
            # 2: timestamp
            # 3: rating

            if int(split[1]) in rating:
                rating[int(split[1])] += 1
            # si no lo hemos visitado lo guardamos
            else:
                rating[int(split[1])] = 1
        
    sorted = sort_recomendations(rating)

    return(sorted)


if __name__ == "__main__":
    nyF = 'recomendation/train_test/Foursquare/US_NewYork/US_NewYork_train.txt'
    nyG = 'recomendation/train_test/Gowalla/US_NewYork/US_NewYork_train.txt'

    tkF = 'recomendation/train_test/Foursquare/JP_Tokyo/JP_Tokyo_train.txt'
    tkG = 'recomendation/train_test/Gowalla/JP_Tokyo/JP_Tokyo_train.txt'

    sfF = 'segunda_parte/recomendation/train_test/Foursquare/US_SanFrancisco/US_SanFrancisco_train.txt'
    sfG = 'segunda_parte/recomendation/train_test/Gowalla/US_SanFrancisco/US_SanFrancisco_train.txt'

    fourNY = venue(nyF)
    gowNY = venue(nyG)

    fourTK = venue(tkF)
    gowTK = venue(tkG)

    fourSF = venue(sfF)
    gowSF = venue(sfG)

    # print("New York:")

    # num = 0
    # poisFNY = set()
    # poisGNY = set()

    # for i in range(0,30):
    #     poisFNY.add(fourNY[i])
    #     poisGNY.add(gowNY[i])
    #     if fourNY[i] == gowNY[i]:
    #         num += 1
    # print('Con orden:', num/30, 'Sin orden:', len(poisFNY & poisGNY)/30)
    #     # print(i, 'Foursquare:', fourNY[i], 'Gowalla:', gowNY[i])

    # print("Tokyo:")

    # num = 0
    # poisFTK = set()
    # poisGTK = set()

    # for i in range(0,30):
    #     poisFTK.add(fourTK[i])
    #     poisGTK.add(gowTK[i])
    #     if fourTK[i] == gowTK[i]:
    #         num += 1
    # print('Con orden:', num/30, 'Sin orden:', len(poisFTK & poisGTK)/30)

    print("San Francisco:")

    num = 0
    poisFSF = set()
    poisGSF = set()

    for i in range(0,30):
        poisFSF.add(fourSF[i])
        poisGSF.add(gowSF[i])
        print(i, 'Foursquare:', fourSF[i], 'Gowalla:', gowSF[i])
        if fourSF[i] == gowSF[i]:
            num += 1
    # print('Con orden:', num/30, 'Sin orden:', len(poisFSF & poisGSF)/30)