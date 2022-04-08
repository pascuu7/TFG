import os

i = 0

contenido = os.listdir('Gowalla/city_checkins/')

pois = {}
users = {}

with open('coincidencias/coincidencias_pois.txt') as fcoin:
    for line_coin in fcoin:
        split_coin = line_coin.split("\t")

        pois[split_coin[0]] = split_coin[1].strip()


with open('coincidencias/coincidencias_users.txt') as fusers:
    for line_users in fusers:
        split_users = line_users.split("\t")

        users[split_users[0]] = split_users[1].strip()

for name in contenido:
    check_gow_file = 'Gowalla/city_checkins/' + name
    file = 'city_checkins/' + name
    
    with open(check_gow_file) as check_gow:
        for line_gow in check_gow:
            split_check = line_gow.split("\t")
            
            if split_check[1] in pois.keys():
                i += 1
                print(str(i) + '\t' + str(split_check) + '\t' + str(pois[split_check[1]]))
                print(str(i) + '\t' + str(split_check) + '\t' + str(users[split_check[0]]) + '\n')
                with open(file, "a") as fcheck:
                    fcheck.write(str(users[split_check[0]]) + '\t' + str(pois[split_check[1]]) + '\t' + str(split_check[2]).strip() + '\n')
                

        

            