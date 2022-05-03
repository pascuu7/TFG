from knn.knn import knn
from popularity.popularity import popularity
from hybrid.hybrid import hybrid

file_ny = 'train_test/US_NewYork/US_NewYork_train.txt'
file_tk = 'train_test/JP_Tokyo/JP_Tokyo_train.txt'
poi_file = '../dataset/Foursquare/POI_city.txt'

# usuario a recomendar
user_in = input("Usuario: ")

popularity_ny, popularity_tk = popularity(file_ny, file_tk, user_in, False)
knn_ny, knn_tk = knn(file_ny, file_tk, user_in, False)

print(popularity_ny, '\n')
print(popularity_tk, '\n')
# print(knn_ny, '\n')
# print(knn_tk)

# hybrid(poi_file, file_ny, file_tk, user_in)



