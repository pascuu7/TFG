def diversity(tipo, recomendations, cutoff):
    recomended = {}

    with open(recomendations) as file:
        for line in file:
            split = line.split("\t")
            # 0: id user
            # 1: id poi
            # 2: rating (menos random y skyline)
            
            if int(split[0]) not in recomended:
                recomended[int(split[0])] = set([int(split[1])])

            else:
                if len(recomended[int(split[0])]) < cutoff:
                    recomended[int(split[0])].add(int(split[1]))

    diver = set()
    for user in recomended:
        diver = diver | recomended[user]

    print('\t', tipo, ':', len(diver))