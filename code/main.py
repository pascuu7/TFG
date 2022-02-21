from geopy.distance import distance
from math import sin, cos, sqrt, atan2, radians


if __name__ == "__main__":
    with open("dataset/POIs.txt") as fpois:
        with open("dataset/cities.txt") as fcities:
            for line_poi in fpois:
                split_poi = line_poi.split("\t")
                print(str(split_poi[3]) + "\n")
                for line_city in fcities:
                    split_city = line_city.split("\t")
                    dist = distance((split_city[1], split_city[2]), (split_poi[1], split_poi[2])).km
                    if dist < 200:
                        print("\t" + str(split_city[0]) + ": " + str(dist))
                    # if distance((split_city[1], split_city[2]), (split_poi[1], split_poi[2])).km < 50:
                    #     file = open("city_files/" + str(split_city[3]) + "_" + str(split_city[0].replace(" ", "")) + ".txt", "w")
                    #     file.write(line_poi)

                break


    # with open("dataset/cities.txt") as fcities:
    #     for line_city in fcities:
    #         split_city = line_city.split("\t")
    #         open("city_files/" + str(split_city[3]) + "_" + str(split_city[0].replace(" ", "")) + ".txt", "w")