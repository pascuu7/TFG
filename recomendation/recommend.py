from knn import knn
from rand import rand
from popularity import popularity
from hybrid import hybrid
from skyline import skyline

# Dataset de Foursquare
train_ny_f = 'train_test/Foursquare/US_NewYork/US_NewYork_train.txt'
train_tk_f = 'train_test/Foursquare/JP_Tokyo/JP_Tokyo_train.txt'
train_sf_f = 'train_test/Foursquare/US_SanFrancisco/US_SanFrancisco_train.txt'

# Dataset de Foursquare + Gowalla
train_ny_g = 'train_test/Gowalla/US_NewYork/US_NewYork_train.txt'
train_tk_g = 'train_test/Gowalla/JP_Tokyo/JP_Tokyo_train.txt'
train_sf_g = 'train_test/Gowalla/US_SanFrancisco/US_SanFrancisco_train.txt'

# # Test (al ser el mismo es indiferente)

test_ny = 'train_test/Gowalla/US_NewYork/US_NewYork_test.txt'
test_tk = 'train_test/Gowalla/JP_Tokyo/JP_Tokyo_test.txt'
test_sf = 'train_test/Gowalla/US_SanFrancisco/US_SanFrancisco_test.txt'

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

# fout_ny_knn_f = 'users_recomendations/Foursquare/Knn/NY_Top50_Knn100.txt'
# fout_tk_knn_f = 'users_recomendations/Foursquare/Knn/TK_Top50_Knn100.txt'
# fout_sf_knn_f = 'users_recomendations/Foursquare/Knn/SF_Top50_Knn10.txt'

# knn(train_ny_f, test_ny, 100, out=fout_ny_knn_f)
# knn(train_tk_f, test_tk, 100, out=fout_tk_knn_f)
# knn(train_sf_f, test_sf, 10, out=fout_sf_knn_f)

# fout_ny_knn_g = 'users_recomendations/Gowalla/Knn/NY_Top50_Knn100.txt'
# fout_tk_knn_g = 'users_recomendations/Gowalla/Knn/TK_Top50_Knn100.txt'
# fout_sf_knn_g = 'users_recomendations/Gowalla/Knn/SF_Top50_Knn10.txt'

# knn(train_ny_g, test_ny, 100, out=fout_ny_knn_g)
# knn(train_tk_g, test_tk, 100, out=fout_tk_knn_g)
# knn(train_sf_g, test_sf, 10, out=fout_sf_knn_g)


# HYBRID

poi_file = '../dataset/Foursquare/POI_city.txt'

# fout_ny_hybrid_f = 'users_recomendations/Foursquare/Hybrid/NY_Top50_knn100.txt'
# fout_tk_hybrid_f = 'users_recomendations/Foursquare/Hybrid/TK_Top50_knn100.txt'
fout_sf_hybrid_f = 'users_recomendations/Foursquare/Hybrid/SF_Top50_knn10.txt'

# hybrid(poi_file, train_ny_f, test_ny, fout_ny_hybrid_f, 10)
# hybrid(poi_file, train_tk_f, test_tk, fout_tk_hybrid_f, 10)
hybrid(poi_file, train_sf_f, test_sf, fout_sf_hybrid_f, 10)

# fout_ny_hybrid_g = 'users_recomendations/Gowalla/Hybrid/NY_Top50_knn100.txt'
# fout_tk_hybrid_g = 'users_recomendations/Gowalla/Hybrid/TK_Top50_knn100.txt'
fout_sf_hybrid_g = 'users_recomendations/Gowalla/Hybrid/SF_Top50_knn10.txt'

# hybrid(poi_file, train_ny_g, test_ny, fout_ny_hybrid_g, 10)
# hybrid(poi_file, train_tk_g, test_tk, fout_tk_hybrid_g, 10)
hybrid(poi_file, train_sf_g, test_sf, fout_sf_hybrid_g, 10)

# RANDOM

# fout_ny_random_f = 'users_recomendations/Foursquare/Random/NY_50.txt'
# fout_tk_random_f = 'users_recomendations/Foursquare/Random/TK_50.txt'
# fout_sf_random_f = 'users_recomendations/Foursquare/Random/SF_50.txt'

# rand(train_ny_f, test_ny_f, fout_ny_random_f)
# rand(train_tk_f, test_tk_f, fout_tk_random_f)
# rand(train_sf_f, test_sf, fout_sf_random_f)

# fout_ny_random_g = 'users_recomendations/Gowalla/Random/NY_50.txt'
# fout_tk_random_g = 'users_recomendations/Gowalla/Random/TK_50.txt'
# fout_sf_random_g = 'users_recomendations/Gowalla/Random/SF_50.txt'

# rand(train_ny_g, test_ny_g, fout_ny_random_g)
# rand(train_tk_g, test_tk_g, fout_tk_random_g)
# rand(train_sf_g, test_sf, fout_sf_random_g)

# Recomendador Skyline

# fout_ny_skyline_f = 'users_recomendations/Foursquare/Skyline/NY_Skyline.txt'
# fout_tk_skyline_f = 'users_recomendations/Foursquare/Skyline/TK_Skyline.txt'
# fout_sf_skyline_f = 'users_recomendations/Foursquare/Skyline/SF_Skyline.txt'

# skyline(train_ny_f, test_ny_f, fout_ny_skyline_f)
# skyline(train_tk_f, test_tk_f, fout_tk_skyline_f)
# skyline(train_sf_f, test_sf_f, fout_sf_skyline_f)

# fout_ny_skyline_g = 'users_recomendations/Gowalla/Skyline/NY_Skyline.txt'
# fout_tk_skyline_g = 'users_recomendations/Gowalla/Skyline/TK_Skyline.txt'
# fout_sf_skyline_g = 'users_recomendations/Gowalla/Skyline/SF_Skyline.txt'

# skyline(train_ny_g, test_ny_g, fout_ny_skyline_g)
# skyline(train_tk_g, test_tk_g, fout_tk_skyline_g)
# skyline(train_sf_g, test_sf_g, fout_sf_skyline_g)