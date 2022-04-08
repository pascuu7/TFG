import os

i = 0

contenido = os.listdir('Foursquare/city_checkins/')

four_users = []
users = {}
gow_users = []

for name in contenido:
    check_four_file = 'Foursquare/city_checkins/' + name
    file = 'city_checkins/' + name
    
    with open(check_four_file) as check_four:
        for line_four in check_four:
            i += 1
            print(i)
            split_check = line_four.split("\t")
            four_users.append(int(split_check[0]))
            if os.path.exists(file):
                with open(file, "a") as fcheck:
                    fcheck.write(line_four)

            else:
                with open(file, "w") as fcheck:
                    fcheck.write(line_four)

max_user = max(four_users)


for name in contenido:
    check_gow_file = 'Gowalla/city_checkins/' + name
    i += 1
    with open(check_gow_file) as check_gow:
        for line_gow in check_gow:
            split_check = line_gow.split("\t")
            if split_check[0] not in gow_users:
                gow_users.append(split_check[0])
                max_user += 1

                if os.path.exists('coincidencias_users.txt'):
                    with open('coincidencias_users.txt', "a") as users:
                        users.write(str(split_check[0]) + '\t' + str(max_user) + '\n')

                else:
                    with open('coincidencias_users.txt', "w") as users:
                        users.write(str(split_check[0]) + '\t' + str(max_user) + '\n')


    print(i)


        

            