import sys

sys.path.append('../')

from functions import read_users

users = set()
visited = {}

def prepare_ex(train):
    with open(train) as file:
        for line in file:
            split = line.split("\t")
            # 0: id user
            # 1: id poi
            # 2: timestamp
            # 3: rating

            users.add(int(split[1]))
            
            if int(split[1]) not in visited:
                visited[int(split[1])] = 1

            else:
                visited[int(split[1])] += 1


def expected_popularity(tipo, recomendations, cutoff):
    recomended = {}
    acum = 0

    with open(recomendations) as file:
        for line in file:
            split = line.split("\t")
            # 0: id user
            # 1: id poi
            # 2: rating (menos random y skyline)

            if int(split[0]) not in recomended:
                recomended[int(split[0])] = set([int(split[1])])
                if int(split[1]) in visited:
                    acum += 1 - (visited[int(split[1])] / len(users))
                else:
                    acum += 1

            else:     
                if len(recomended[int(split[0])]) < cutoff:    
                    recomended[int(split[0])].add(int(split[1]))

                    if int(split[1]) in visited:
                        acum += 1 - (visited[int(split[1])] / len(users))
                    else:
                        acum += 1


    print('\t', tipo, ':', acum/len(recomended))


