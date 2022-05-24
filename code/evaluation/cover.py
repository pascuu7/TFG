def cover(tipo, recomendations):
    users = set()
    with open(recomendations) as file:
        for line in file:
            split = line.split("\t")
            # 0: id user
            # 1: id poi
            # 2: rating (menos random y skyline)

            
            users.add(int(split[0]))


    print('\t', tipo, ':', len(users))