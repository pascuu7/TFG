from knn.knn import knn
from popularity.popularity import popularity
from hybrid.hybrid import hybrid

test_ny = 'train_test/US_NewYork/US_NewYork_train.txt'
out = 'users_recomendations/NY_Popularity_Top50_RepeatedScoreTrue.txt'

poi_file = '../dataset/Foursquare/POI_city.txt'


popularity_ny = popularity(test_ny, out)
knn_ny = knn(test_ny, out)

print(popularity_ny, '\n')
print(knn_ny, '\n')


# hybrid(poi_file, file_ny, file_tk, user_in)



