from knn.knn import knn
from rand.rand import rand
from popularity.popularity import popularity
from hybrid.hybrid import hybrid
from skyline.skyline import skyline

# FOURSQUARE

train_sf = 'train_test/Foursquare/US_SanFrancisco/US_SanFrancisco_train.txt'
test_sf = 'train_test/Foursquare/US_SanFrancisco/US_SanFrancisco_test.txt'


# GOWALLA + FOURSQUARE

# train_sf = 'train_test/Gowalla/US_SanFrancisco/US_SanFrancisco_train.txt'
# test_sf = 'train_test/Gowalla/US_SanFrancisco/US_SanFrancisco_test.txt'



# POPULARIDAD

# fout_sf_true_pop = 'users_recomendations/Gowalla/Popularity/SF_Top50_RepeatedScoreTrue.txt'
# fout_sf_false_pop = 'users_recomendations/Gowalla/Popularity/SF_Top50_RepeatedScoreFalse.txt'

# popularity(train_sf, test_sf, out=fout_sf_false_pop)
# popularity(train_sf, test_sf, out=fout_sf_true_pop, repeated=True)



# KNN

# fout_sf_knn = 'users_recomendations/Gowalla/Knn/SF_Top50_Knn50.txt'

# knn(train_sf, test_sf, 50, out=fout_sf_knn)


# RANDOM

# fout_sf_random = 'users_recomendations/Gowalla/Random/SF_50.txt'

# random_tk = rand(train_sf, test_sf, fout_sf_random)



# HYBRID

poi_file = '../dataset/POI_city.txt'

fout_sf_hybrid = 'users_recomendations/Foursquare/Hybrid/SF_Top50_knn50.txt'

hybrid_tk = hybrid(poi_file, train_sf, test_sf, fout_sf_hybrid, 50)



# SKYLINE

# fout_sf_skyline = 'users_recomendations/Foursquare/Skyline/SF_Skyline.txt'

# skyline_tk = skyline(train_sf, test_sf, fout_sf_skyline)