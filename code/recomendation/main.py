from knn.knn import knn
from rand.rand import rand
from popularity.popularity import popularity
from hybrid.hybrid import hybrid
from skyline.skyline import skyline

# FOURSQUARE

train_ny = 'train_test/Gowalla/US_NewYork/US_NewYork_train.txt'
train_tk = 'train_test/Gowalla/JP_Tokyo/JP_Tokyo_train.txt'

test_ny = 'train_test/Gowalla/US_NewYork/US_NewYork_test.txt'
test_tk = 'train_test/Gowalla/JP_Tokyo/JP_Tokyo_test.txt'


# GOWALLA + FOURSQUARE

# train_ny = 'train_test/Gowalla/US_NewYork/US_NewYork_train.txt'
# train_tk = 'train_test/Gowalla/JP_Tokyo/JP_Tokyo_train.txt'

# test_ny = 'train_test/Gowalla/US_NewYork/US_NewYork_test.txt'
# test_tk = 'train_test/Gowalla/JP_Tokyo/JP_Tokyo_test.txt'



# POPULARIDAD

# # fout_ny_true_pop = 'users_recomendations/Gowalla/Popularity/NY_Top50_RepeatedScoreTrue.txt'
# # fout_tk_true_pop = 'users_recomendations/Gowalla/Popularity/TK_Top50_RepeatedScoreTrue.txt'
# fout_ny_false_pop = 'users_recomendations/Gowalla/Popularity/NY_Top50_RepeatedScoreFalse.txt'
# # fout_tk_false_pop = 'users_recomendations/Gowalla/Popularity/TK_Top50_RepeatedScoreFalse.txt'

# popularity_ny = popularity(train_ny, test_ny, out=fout_ny_false_pop)
# # popularity_tk = popularity(train_tk, test_tk, out=fout_tk_true_pop, repeated=True)



# KNN

# # fout_ny_knn = 'users_recomendations/Gowalla/Knn/NY_Top50_Knn40.txt'
# fout_tk_knn = 'users_recomendations/Gowalla/Knn/TK_Top50_Knn100.txt'

# # knn(train_ny, test_ny, 40, out=fout_ny_knn)
# knn(train_tk, test_tk, 100, out = fout_tk_knn)


# RANDOM

# fout_ny_random = 'users_recomendations/Gowalla/Random/NY_50.txt'
# fout_tk_random = 'users_recomendations/Gowalla/Random/TK_50.txt'

# random_ny = rand(train_ny, test_ny, fout_ny_random)
# random_tk = rand(train_tk, test_tk, fout_tk_random)



# HYBRID

poi_file = '../dataset/POI_city.txt'

# fout_ny_hybrid = 'users_recomendations/Gowalla/Hybrid/NY_Top50_knn100.txt'
fout_tk_hybrid = 'users_recomendations/Gowalla/Hybrid/TK_Top50_knn5.txt'

# hybrid_ny = hybrid(poi_file, train_ny, test_ny, fout_ny_hybrid, 100)
hybrid_tk = hybrid(poi_file, train_tk, test_tk, fout_tk_hybrid, 5)



# SKYLINE

# fout_ny_skyline = 'users_recomendations/Gowalla/Skyline/NY_Skyline.txt'
# # fout_tk_skyline = 'users_recomendations/Gowalla/Skyline/TK_Skyline.txt'

# skyline_ny = skyline(train_ny, test_ny, fout_ny_skyline)
# # skyline_tk = skyline(train_tk, test_tk, fout_tk_skyline)