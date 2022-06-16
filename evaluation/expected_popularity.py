import sys

sys.path.append('../')

from functions import read_users

def expected_popularity(tipo, recomendations, test, train, cutoff):
    users_train = set() # usuarios de entrenamiento
    users_test = read_users(test) # ususarios de test
    
    # usuarios que han visitado cierto poi
    visited = {} # id_poi: [id_user1, id_user2]
    # pois recomendados
    recomended = {} # id_user_ [id_poi1, id_poi2]

    with open(train) as file:
        for line in file:
            split = line.split("\t")
            # 0: id user
            # 1: id poi
            # 2: timestamp
            # 3: rating

            users_train.add(int(split[0]))
            
            if int(split[1]) not in visited:
                visited[int(split[1])] = set([int(split[0])])

            else:
                visited[int(split[1])].add(int(split[0]))

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
    eval = 0
    for user in recomended:
        acum = 0
        for poi in recomended[user]:
            if poi in visited:
                acum += 1 - (len(visited[poi])/ len(users_train))
            else:
                acum += 1
        eval += acum/len(recomended[user])

    print('\t', tipo, ':', eval/len(recomended))


