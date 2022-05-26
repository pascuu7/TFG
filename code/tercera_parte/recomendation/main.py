from knn.knn import knn
from rand.rand import rand
from popularity.popularity import popularity
from hybrid.hybrid import hybrid
from skyline.skyline import skyline

# FOURSQUARE + GOWALLA

train_ny = 'train_test/Foursquare/US_NewYork/train.txt'
train_tk = 'train_test/Foursquare/JP_Tokyo/train.txt'
train_sf = 'train_test/Foursquare/US_SanFrancisco/train.txt'

test_ny = 'train_test/Foursquare/US_NewYork/test.txt'
test_tk = 'train_test/Foursquare/JP_Tokyo/test.txt'
test_sf = 'train_test/Foursquare/US_SanFrancisco/test.txt'


# GOWALLA

# train_ny = 'train_test/Gowalla/US_NewYork/train.txt'
# train_tk = 'train_test/Gowalla/JP_Tokyo/train.txt'
# train_sf = 'train_test/Gowalla/US_SanFrancisco/train.txt'

# test_ny = 'train_test/Gowalla/US_NewYork/test.txt'
# test_tk = 'train_test/Gowalla/JP_Tokyo/test.txt'
# test_sf = 'train_test/Gowalla/US_SanFrancisco/test.txt'



# POPULARIDAD

# fout_ny_true_pop = 'users_recomendations/Foursquare/Popularity/NY_Top50_RepeatedScoreTrue.txt'
# # fout_tk_true_pop = 'users_recomendations/Foursquare/Popularity/TK_Top50_RepeatedScoreTrue.txt'
# # # fout_sf_true_pop = 'users_recomendations/Gowalla/Popularity/Sf_Top50_RepeatedScoreTrue.txt'

# # fout_ny_false_pop = 'users_recomendations/Foursquare/Popularity/NY_Top50_RepeatedScoreFalse.txt'
# # # fout_tk_false_pop = 'users_recomendations/Foursquare/Popularity/TK_Top50_RepeatedScoreFalse.txt'
# # # fout_sf_false_pop = 'users_recomendations/Gowalla/Popularity/SF_Top50_RepeatedScoreFalse.txt'

# popularity_ny = popularity(train_ny, test_ny, out=fout_ny_true_pop, repeated=True)
# # popularity_tk = popularity(train_tk, test_tk, out=fout_tk_true_pop, repeated=True)
# # popularity_sf = popularity(train_sf, test_sf, out=fout_sf_true_pop, repeated=True)



# KNN

# # fout_ny_knn = 'users_recomendations/Foursquare/Knn/NY_Top50_Knn50.txt'
# fout_tk_knn = 'users_recomendations/Gowalla/Knn/TK_Top50_Knn5.txt'
# # # fout_sf_knn = 'users_recomendations/Gowalla/Knn/SF_Top50_Knn100.txt'

# # knn(train_ny, test_ny, 50, out=fout_ny_knn)
# knn(train_tk, test_tk, 5, out = fout_tk_knn)
# # # # knn(train_sf, test_sf, 100, out = fout_sf_knn)


# RANDOM

# # fout_ny_random = 'users_recomendations/Gowalla/Random/NY_50.txt'
# fout_tk_random = 'users_recomendations/Foursquare/Random/TK_50.txt'
# # fout_sf_random = 'users_recomendations/Gowalla/Random/SF_50.txt'

# # random_ny = rand(train_ny, test_ny, fout_ny_random)
# random_tk = rand(train_tk, test_tk, fout_tk_random)
# # random_sf = rand(train_sf, test_sf, fout_sf_random)



# HYBRID

poi_file = '../dataset/POI_city.txt'

# fout_ny_hybrid = 'users_recomendations/Gowalla/Hybrid/NY_Top50_knn50.txt'
fout_tk_hybrid = 'users_recomendations/Foursquare/Hybrid/TK_Top50_knn5.txt'
# fout_sf_hybrid = 'users_recomendations/Gowalla/Hybrid/SF_Top50_knn100.txt'

# hybrid_ny = hybrid(poi_file, train_ny, test_ny, fout_ny_hybrid, 50)
hybrid_tk = hybrid(poi_file, train_tk, test_tk, fout_tk_hybrid, 5)
# hybrid_sf = hybrid(poi_file, train_sf, test_sf, fout_sf_hybrid, 100)



# SKYLINE

# fout_ny_skyline = 'users_recomendations/Foursquare/Skyline/NY_Skyline.txt'
# # fout_tk_skyline = 'users_recomendations/Foursquare/Skyline/TK_Skyline.txt'
# # fout_sf_skyline = 'users_recomendations/Gowalla/Skyline/SF_Skyline.txt'

# skyline_ny = skyline(train_ny, test_ny, fout_ny_skyline)
# # skyline_tk = skyline(train_tk, test_tk, fout_tk_skyline)
# # skyline_sf = skyline(train_sf, test_sf, fout_sf_skyline)