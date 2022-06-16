from knn.knn import knn
from rand.rand import rand
from popularity.popularity import popularity
from hybrid.hybrid import hybrid
from skyline.skyline import skyline

# Dataset de Foursquare
train_ny_f = 'train_test/Foursquare/US_NewYork/US_NewYork_train.txt'
train_tk_f = 'train_test/Foursquare/JP_Tokyo/JP_Tokyo_train.txt'
train_sf_f = 'train_test/Foursquare/US_SanFrancisco/US_SanFrancisco_train.txt'

test_ny_f = 'train_test/Foursquare/US_NewYork/US_NewYork_test.txt'
test_tk_f = 'train_test/Foursquare/JP_Tokyo/JP_Tokyo_test.txt'
test_sf_f = 'train_test/Foursquare/US_SanFrancisco/US_SanFrancisco_test.txt'

# Dataset de Foursquare + Gowalla
train_ny_g = 'train_test/Gowalla/US_NewYork/US_NewYork_train.txt'
train_tk_g = 'train_test/Gowalla/JP_Tokyo/JP_Tokyo_train.txt'
train_sf_g = 'train_test/Gowalla/US_SanFrancisco/US_SanFrancisco_train.txt'

test_ny_g = 'train_test/Gowalla/US_NewYork/US_NewYork_test.txt'
test_tk_g = 'train_test/Gowalla/JP_Tokyo/JP_Tokyo_test.txt'
test_sf_g = 'train_test/Gowalla/US_SanFrancisco/US_SanFrancisco_test.txt'



# # Recomendador de popularidad

# # Foursquare
# # Nombres de los ficheros de salida
# fout_ny_true_pop_f = 'users_recomendations/Foursquare/Popularity/NY_Top50_RepeatedScoreTrue.txt'
# fout_tk_true_pop_f = 'users_recomendations/Foursquare/Popularity/TK_Top50_RepeatedScoreTrue.txt'
# fout_sf_true_pop_f = 'users_recomendations/Foursquare/Popularity/SF_Top50_RepeatedScoreTrue.txt'

# fout_ny_false_pop_f = 'users_recomendations/Foursquare/Popularity/NY_Top50_RepeatedScoreFalse.txt'
# fout_tk_false_pop_f = 'users_recomendations/Foursquare/Popularity/TK_Top50_RepeatedScoreFalse.txt'
# fout_sf_false_pop_f = 'users_recomendations/Foursquare/Popularity/SF_Top50_RepeatedScoreFalse.txt'

# # Popularidad sin elementos repetidos
# popularity(train_ny_f, test_ny_f, out=fout_ny_false_pop_f)
# popularity(train_tk_f, test_tk_f, out=fout_tk_false_pop_f)
# popularity(train_sf_f, test_sf_f, out=fout_sf_false_pop_f)

# # Popularidad con elementos repetidos
# popularity(train_ny_f, test_ny_f, out=fout_ny_true_pop_f, repeated=True)
# popularity(train_tk_f, test_tk_f, out=fout_tk_true_pop_f, repeated=True)
# popularity(train_sf_f, test_sf_f, out=fout_sf_true_pop_f, repeated=True)

# # Foursquare + Gowalla
# # Nombres de los ficheros de salida
# fout_ny_true_pop_g = 'users_recomendations/Gowalla/Popularity/NY_Top50_RepeatedScoreTrue.txt'
# fout_tk_true_pop_g = 'users_recomendations/Gowalla/Popularity/TK_Top50_RepeatedScoreTrue.txt'
# fout_sf_true_pop_g = 'users_recomendations/Gowalla/Popularity/SF_Top50_RepeatedScoreTrue.txt'

# fout_ny_false_pop_g = 'users_recomendations/Gowalla/Popularity/NY_Top50_RepeatedScoreFalse.txt'
# fout_tk_false_pop_g = 'users_recomendations/Gowalla/Popularity/TK_Top50_RepeatedScoreFalse.txt'
# fout_sf_false_pop_g = 'users_recomendations/Gowalla/Popularity/SF_Top50_RepeatedScoreFalse.txt'

# # Popularidad sin elementos repetidos
# popularity(train_ny_g, test_ny_g, out=fout_ny_false_pop_g)
# popularity(train_tk_g, test_tk_g, out=fout_tk_false_pop_g)
# popularity(train_sf_g, test_sf_g, out=fout_sf_false_pop_g)

# # Popularidad con elementos repetidos
# popularity(train_ny_g, test_ny_g, out=fout_ny_true_pop_g, repeated=True)
# popularity(train_tk_g, test_tk_g, out=fout_tk_true_pop_g, repeated=True)
# popularity(train_sf_g, test_sf_g, out=fout_sf_true_pop_g, repeated=True)




# KNN

# fout_ny_knn = 'users_recomendations/Gowalla/Knn/NY_Top50_Knn100.txt'
# fout_tk_knn = 'users_recomendations/Gowalla/Knn/TK_Top50_Knn100.txt'
# fout_sf_knn = 'users_recomendations/Gowalla/Knn/SF_Top50_Knn100.txt'

# knn(train_ny_f, test_ny_f, 100, out=fout_ny_knn)
# knn(train_tk_f, test_tk_f, 100, out=fout_tk_knn)


# RANDOM

# # fout_ny_random = 'users_recomendations/Gowalla/Random/NY_50.txt'
# fout_tk_random = 'users_recomendations/Gowalla/Random/TK_50.txt'

# # random_ny = rand(train_ny, test_ny, fout_ny_random)
# random_tk = rand(train_tk, test_tk, fout_tk_random)



# HYBRID

# poi_file = '../dataset/POI_city.txt'

# # fout_ny_hybrid = 'users_recomendations/Gowalla/Hybrid/NY_Top50_knn50.txt'
# fout_tk_hybrid = 'users_recomendations/Gowalla/Hybrid/TK_Top50_knn100.txt'

# # hybrid_ny = hybrid(poi_file, train_ny, test_ny, fout_ny_hybrid, 50)
# hybrid_tk = hybrid(poi_file, train_tk, test_tk, fout_tk_hybrid, 100)


# Recomendador Skyline

fout_ny_skyline_f = 'users_recomendations/Foursquare/Skyline/NY_Skyline.txt'
fout_tk_skyline_f = 'users_recomendations/Foursquare/Skyline/TK_Skyline.txt'
fout_sf_skyline_f = 'users_recomendations/Foursquare/Skyline/SF_Skyline.txt'

fout_ny_skyline_g = 'users_recomendations/Gowalla/Skyline/NY_Skyline.txt'
fout_tk_skyline_g = 'users_recomendations/Gowalla/Skyline/TK_Skyline.txt'
fout_sf_skyline_g = 'users_recomendations/Gowalla/Skyline/SF_Skyline.txt'

skyline_ny = skyline(train_ny, test_ny, fout_ny_skyline)
skyline_tk = skyline(train_tk, test_tk, fout_tk_skyline)