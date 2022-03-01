i = 0

with open('dataset/checkins.txt') as fcheck:
    with open('city_pois') as fpois:
        for line_check in fcheck:
            split_check = line_check.split("\t")
            for line_pois in fpois:
                split_pois = line_check.split("\t")
                if split_pois[1] == split_check[1]:
                    pass

                    # print(i)
                    # i += 1
            # print(str(i) + '\t' +  str(split_check))
            # i += 1