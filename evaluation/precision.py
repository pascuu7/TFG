def precision(tipo, recomendations, test, cutoff):
    recomended = {}
    visited = {}
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

    with open(test) as file:
        for line in file:
            split = line.split("\t")
            # 0: id user
            # 1: id poi
            # 2: timestamp
            # 3: rating
            
            if int(split[0]) not in visited:
                visited[int(split[0])] = set([int(split[1])])

            else:
                visited[int(split[0])].add(int(split[1]))

    eval = 0
    for user in recomended:
        eval += len(recomended[user] & visited[user])/cutoff

    print('\t', tipo, ':', eval / len(recomended))



