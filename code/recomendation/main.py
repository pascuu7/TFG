from knn.knn import knn
from rand.rand import rand
from popularity.popularity import popularity
from hybrid.hybrid import hybrid
from skyline.skyline import skyline

train_ny = 'train_test/US_NewYork/US_NewYork_train.txt'
train_tk = 'train_test/JP_Tokyo/JP_Tokyo_train.txt'

test_ny = 'train_test/US_NewYork/US_NewYork_test.txt'
test_tk = 'train_test/JP_Tokyo/JP_Tokyo_test.txt'



# POPULARIDAD

# fout_ny_true_pop = 'users_recomendations/Popularity/NY_Top50_RepeatedScoreTrue.txt'
# fout_tk_true_pop = 'users_recomendations/Popularity/TK_Top50_RepeatedScoreTrue.txt'
# fout_ny_false_pop = 'users_recomendations/Popularity/NY_Top50_RepeatedScoreFalse.txt'
# fout_tk_false_pop = 'users_recomendations/Popularity/TK_Top50_RepeatedScoreFalse.txt'

# popularity_ny = popularity(train_ny, test_ny, out=fout_ny_false_pop)
# popularity_tk = popularity(train_tk, test_tk, out=fout_tk_false_pop)



# KNN

# fout_ny_knn = 'users_recomendations/Knn/NY_Top50_Knn90.txt'
# fout_tk_knn = 'users_recomendations/Knn/TK_Top50_Knn10.txt'

# knn_ny = (train_ny, test_ny, 90, out = fout_ny_knn)
# knn_tk = (train_tk, test_tk, 10, out = fout_tk_knn)



# RANDOM

# fout_ny_random = 'users_recomendations/Random/NY_50.txt'
fout_tk_random = 'users_recomendations/Random/TK_50.txt'

# random_ny = rand(train_ny, test_ny, fout_ny_random)
random_tk = rand(train_tk, test_tk, fout_tk_random)



# HYBRID

# poi_file = '../dataset/Foursquare/POI_city.txt'

# fout_ny_hybrid = 'users_recomendations/Hybrid/NY_Top50_knn5.txt'
# fout_tk_hybrid = 'users_recomendations/Hybrid/TK_Top50_knn5.txt'

# hybrid_ny = hybrid(poi_file, train_ny, test_ny, fout_ny_hybrid, 5)
# hybrid_tk = hybrid(poi_file, train_tk, test_tk, fout_tk_hybrid, 5)



# SKYLINE

# fout_ny_skyline = 'users_recomendations/Skyline/NY_Skyline.txt'
# fout_tk_skyline = 'users_recomendations/Skyline/TK_Skyline.txt'

# skyline_ny = skyline(train_ny, test_ny, fout_ny_skyline)
# skyline_tk = skyline(train_tk, test_tk, fout_tk_skyline)







