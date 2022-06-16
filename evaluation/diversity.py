def diversity(tipo, recomendations):
    recomended = set()

    with open(recomendations) as file:
        for line in file:
            split = line.split("\t")
            # 0: id user
            # 1: id poi
            # 2: rating (menos random y skyline)
            
            recomended.add(int(split[1]))

    print('\t', tipo, ':', len(recomended))