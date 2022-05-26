from cover import cover
from precision import precision
from recall import recall
from diversity import diversity
from expected_popularity import expected_popularity

# NEW YORK

test_sf = '../recomendation/train_test/Gowalla/US_SanFrancisco/US_SanFrancisco_test.txt'
train_sf_four = '../recomendation/train_test/Foursquare/US_SanFrancisco/US_SanFrancisco_train.txt'
train_sf_gow = '../recomendation/train_test/Gowalla/US_SanFrancisco/US_SanFrancisco_train.txt'


recomendationPOPGow = '../recomendation/users_recomendations/Gowalla/Popularity/SF_Top50_RepeatedScoreTrue.txt'
recomendationPOPFour = '../recomendation/users_recomendations/Foursquare/Popularity/SF_Top50_RepeatedScoreTrue.txt'

recomendationKNNGow = '../recomendation/users_recomendations/Gowalla/Knn/SF_Top50_Knn50.txt'
recomendationKNNFour = '../recomendation/users_recomendations/Foursquare/Knn/SF_Top50_Knn50.txt'

recomendationHYBRIDGow = '../recomendation/users_recomendations/Gowalla/Hybrid/SF_Top50_knn50.txt'
recomendationHYBRIDFour = '../recomendation/users_recomendations/Foursquare/Hybrid/SF_Top50_knn50.txt'

recomendationRANDOMGow = '../recomendation/users_recomendations/Gowalla/Random/SF_50.txt'
recomendationRANDOMFour = '../recomendation/users_recomendations/Foursquare/Random/SF_50.txt'

recomendationSKYLINEGow = '../recomendation/users_recomendations/Gowalla/Skyline/SF_Skyline.txt'
recomendationSKYLINEFour = '../recomendation/users_recomendations/Foursquare/Skyline/SF_Skyline.txt'

cutoff = 10

print('Precision:')

print(' Foursquare')

precision('Random', recomendationRANDOMFour, test_sf, cutoff)
precision('Skyline', recomendationSKYLINEFour, test_sf, cutoff)
precision('Popularity', recomendationPOPFour, test_sf, cutoff)
precision('Knn', recomendationKNNFour, test_sf, cutoff)
precision('Hybrid', recomendationHYBRIDFour, test_sf, cutoff)

print(' Gowalla:')

precision('Random', recomendationRANDOMGow, test_sf, cutoff)
precision('Skyline', recomendationSKYLINEGow, test_sf, cutoff)
precision('Popularity', recomendationPOPGow, test_sf, cutoff)
precision('Knn', recomendationKNNGow, test_sf, cutoff)
precision('Hybrid', recomendationHYBRIDGow, test_sf, cutoff)


print('Recall:')

print(' Foursquare')

recall('Random', recomendationRANDOMFour, test_sf, cutoff)
recall('Skyline', recomendationSKYLINEFour, test_sf, cutoff)
recall('Popularity', recomendationPOPFour, test_sf, cutoff)
recall('Knn', recomendationKNNFour, test_sf, cutoff)
recall('Hybrid', recomendationHYBRIDFour, test_sf, cutoff)

print(' Gowalla:')

recall('Random', recomendationRANDOMGow, test_sf, cutoff)
recall('Skyline', recomendationSKYLINEGow, test_sf, cutoff)
recall('Popularity', recomendationPOPGow, test_sf, cutoff)
recall('Knn', recomendationKNNGow, test_sf, cutoff)
recall('Hybrid', recomendationHYBRIDGow, test_sf, cutoff)

print('\n')

print('Agregate diversity:')

print(' Foursquare')

diversity('Random', recomendationRANDOMFour)
diversity('Skyline', recomendationSKYLINEFour)
diversity('Popularity', recomendationPOPFour)
diversity('Knn', recomendationKNNFour)
diversity('Hybrid', recomendationHYBRIDFour)

print(' Gowalla:')

diversity('Random', recomendationRANDOMGow)
diversity('Skyline', recomendationSKYLINEGow)
diversity('Popularity', recomendationPOPGow)
diversity('Knn', recomendationKNNGow)
diversity('Hybrid', recomendationHYBRIDGow)

print('\n')

print('Coverage:')

print(' Foursquare')

cover('Random', recomendationRANDOMFour)
cover('Skyline', recomendationSKYLINEFour)
cover('Popularity', recomendationPOPFour)
cover('Knn', recomendationKNNFour)
cover('Hybrid', recomendationHYBRIDFour)

print(' Gowalla:')

cover('Random', recomendationRANDOMGow)
cover('Skyline', recomendationSKYLINEGow)
cover('Popularity', recomendationPOPGow)
cover('Knn', recomendationKNNGow)
cover('Hybrid', recomendationHYBRIDGow)

print('\n')

print('Expected popularity:')

print(' Foursquare')

expected_popularity('Random', recomendationRANDOMFour, test_sf, train_sf_four, cutoff)
expected_popularity('Skyline', recomendationSKYLINEFour, test_sf, train_sf_four, cutoff)
expected_popularity('Popularity', recomendationPOPFour, test_sf, train_sf_four, cutoff)
expected_popularity('Knn', recomendationKNNFour, test_sf, train_sf_four, cutoff)
expected_popularity('Hybrid', recomendationHYBRIDFour, test_sf, train_sf_four, cutoff)

print(' Gowalla:')

expected_popularity('Random', recomendationRANDOMGow, test_sf, train_sf_gow, cutoff)
expected_popularity('Skyline', recomendationSKYLINEGow, test_sf, train_sf_gow, cutoff)
expected_popularity('Popularity', recomendationPOPGow, test_sf, train_sf_gow, cutoff)
expected_popularity('Knn', recomendationKNNGow, test_sf, train_sf_gow, cutoff)
expected_popularity('Hybrid', recomendationHYBRIDGow, test_sf, train_sf_gow, cutoff)
