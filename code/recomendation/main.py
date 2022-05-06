from knn.knn import knn
from popularity.popularity import popularity
from hybrid.hybrid import hybrid

train_ny = 'train_test/US_NewYork/US_NewYork_train.txt'
out = 'users_recomendations/NY_Popularity_Top50_RepeatedScoreTrue.txt'

poi_file = '../dataset/Foursquare/POI_city.txt'


popularity_ny = popularity(train_ny, out)
knn_ny = knn(train_ny, out)
hybrid_ny = hybrid(poi_file, train_ny, out)

# print(popularity_ny, '\n')
# print(knn_ny, '\n')
print(hybrid_ny, '\n')






