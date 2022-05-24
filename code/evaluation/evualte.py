from cover import cover
from precision import precision
from recall import recall
from diversity import diversity
from expected_popularity import expected_popularity

test_ny = '../recomendation/train_test/Gowalla/US_NewYork/US_NewYork_test.txt'
train_ny_four = '../recomendation/train_test/Foursquare/US_NewYork/US_NewYork_train.txt'
train_ny_gow = '../recomendation/train_test/Gowalla/US_NewYork/US_NewYork_train.txt'


recomendationPOPGow = '../recomendation/users_recomendations/Gowalla/Popularity/NY_Top50_RepeatedScoreTrue.txt'
recomendationPOPFour = '../recomendation/users_recomendations/Foursquare/Popularity/NY_Top50_RepeatedScoreTrue.txt'

recomendationKNNGow = '../recomendation/users_recomendations/Gowalla/Knn/NY_Top50_Knn50.txt'
recomendationKNNFour = '../recomendation/users_recomendations/Foursquare/Knn/NY_Top50_Knn50.txt'

recomendationHYBRIDGow = '../recomendation/users_recomendations/Gowalla/Hybrid/NY_Top50_knn50.txt'
recomendationHYBRIDFour = '../recomendation/users_recomendations/Foursquare/Hybrid/NY_Top50_knn50.txt'

recomendationRANDOMGow = '../recomendation/users_recomendations/Gowalla/Random/NY_50.txt'
recomendationRANDOMFour = '../recomendation/users_recomendations/Foursquare/Random/NY_50.txt'

recomendationSKYLINEGow = '../recomendation/users_recomendations/Gowalla/Skyline/NY_Skyline.txt'
recomendationSKYLINEFour = '../recomendation/users_recomendations/Foursquare/Skyline/NY_Skyline.txt'

cutoff = 10


print('FOURSQUARE con cuttoff', cutoff, ':\n')


print('Precision:')

precision('Random', recomendationRANDOMFour, test_ny, cutoff)
precision('Skyline', recomendationSKYLINEFour, test_ny, cutoff)
precision('Popularity', recomendationPOPFour, test_ny, cutoff)
precision('Knn', recomendationKNNFour, test_ny, cutoff)
precision('Hybrid', recomendationHYBRIDFour, test_ny, cutoff)

print('Recall:')

recall('Random', recomendationRANDOMFour, test_ny, cutoff)
recall('Skyline', recomendationSKYLINEFour, test_ny, cutoff)
recall('Popularity', recomendationPOPFour, test_ny, cutoff)
recall('Knn', recomendationKNNFour, test_ny, cutoff)
recall('Hybrid', recomendationHYBRIDFour, test_ny, cutoff)

print('Agregate diversity:')

diversity('Random', recomendationRANDOMFour)
diversity('Skyline', recomendationSKYLINEFour)
diversity('Popularity', recomendationPOPFour)
diversity('Knn', recomendationKNNFour)
diversity('Hybrid', recomendationHYBRIDFour)

print('Coverage:')

cover('Random', recomendationRANDOMFour)
cover('Skyline', recomendationSKYLINEFour)
cover('Popularity', recomendationPOPFour)
cover('Knn', recomendationKNNFour)
cover('Hybrid', recomendationHYBRIDFour)

print('Expected popularity:')

expected_popularity('Random', recomendationRANDOMFour, test_ny, train_ny_four, cutoff)
expected_popularity('Skyline', recomendationSKYLINEFour, test_ny, train_ny_four, cutoff)
expected_popularity('Popularity', recomendationPOPFour, test_ny, train_ny_four, cutoff)
expected_popularity('Knn', recomendationKNNFour, test_ny, train_ny_four, cutoff)
expected_popularity('Hybrid', recomendationHYBRIDFour, test_ny, train_ny_four, cutoff)


print('GOWALLA con cutoff', cutoff, ':\n')

print('Precision:')

precision('Random', recomendationRANDOMGow, test_ny, cutoff)
precision('Skyline', recomendationSKYLINEGow, test_ny, cutoff)
precision('Popularity', recomendationPOPGow, test_ny, cutoff)
precision('Knn', recomendationKNNGow, test_ny, cutoff)
precision('Hybrid', recomendationHYBRIDGow, test_ny, cutoff)

print('Recall:')

recall('Random', recomendationRANDOMGow, test_ny, cutoff)
recall('Skyline', recomendationSKYLINEGow, test_ny, cutoff)
recall('Popularity', recomendationPOPGow, test_ny, cutoff)
recall('Knn', recomendationKNNGow, test_ny, cutoff)
recall('Hybrid', recomendationHYBRIDGow, test_ny, cutoff)

print('Agregate diversity:')

diversity('Random', recomendationRANDOMGow)
diversity('Skyline', recomendationSKYLINEGow)
diversity('Popularity', recomendationPOPGow)
diversity('Knn', recomendationKNNGow)
diversity('Hybrid', recomendationHYBRIDGow)

print('Coverage:')

cover('Random', recomendationRANDOMFour)
cover('Skyline', recomendationSKYLINEFour)
cover('Popularity', recomendationPOPGow)
cover('Knn', recomendationKNNGow)
cover('Hybrid', recomendationHYBRIDFour)

print('Expected popularity:')

expected_popularity('Random', recomendationRANDOMFour, test_ny, train_ny_gow, cutoff)
expected_popularity('Skyline', recomendationSKYLINEFour, test_ny, train_ny_gow, cutoff)
expected_popularity('Popularity', recomendationPOPFour, test_ny, train_ny_gow, cutoff)
expected_popularity('Knn', recomendationKNNFour, test_ny, train_ny_gow, cutoff)
expected_popularity('Hybrid', recomendationHYBRIDFour, test_ny, train_ny_gow, cutoff)
