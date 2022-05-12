from knn.knn import knn
from popularity.popularity import popularity
from hybrid.hybrid import hybrid


train_ny = 'train_test/US_NewYork/US_NewYork_train.txt'
train_tk = 'train_test/JP_Tokyo/JP_Tokyo_train.txt'

test_ny = 'train_test/US_NewYork/US_NewYork_test.txt'
test_tk = 'train_test/JP_Tokyo/JP_Tokyo_test.txt'

fout_ny_true_pop = 'users_recomendations/Popularity/NY_Top50_RepeatedScoreTrue.txt'
fout_tk_true_pop = 'users_recomendations/Popularity/TK_Top50_RepeatedScoreTrue.txt'

fout_ny_false_pop = 'users_recomendations/Popularity/NY_Top50_RepeatedScoreFalse.txt'
fout_tk_false_pop = 'users_recomendations/Popularity/TK_Top50_RepeatedScoreFalse.txt'

poi_file = '../dataset/Foursquare/POI_city.txt'

popularity_ny = popularity(train_tk, test_tk, fout_ny_false_pop, False)
# knn_ny = knn(train_ny, out)
# hybrid_ny = hybrid(poi_file, train_ny, out)

# print(popularity_ny, '\n')
# print(knn_ny, '\n')
# print(hybrid_ny, '\n')






