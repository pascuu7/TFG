from cover import cover
from precision import precision
from recall import recall
from diversity import diversity
from expected_popularity import expected_popularity, prepare_ex

test_ny = '../recomendation/train_test/Gowalla/US_NewYork/US_NewYork_test.txt'
train_ny_four = '../recomendation/train_test/Foursquare/US_NewYork/US_NewYork_train.txt'

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


print('FOURSQUARE con cuttoff:', cutoff, '\n')

print('Expected popularity:')

# prepare_ex(train_ny_four)

# expected_popularity('Random', recomendationRANDOMFour, cutoff)
# expected_popularity('Skyline', recomendationSKYLINEFour, cutoff)
# expected_popularity('Popularity', recomendationPOPFour, cutoff)
# expected_popularity('Knn', recomendationKNNFour, cutoff)
# expected_popularity('Hybrid', recomendationHYBRIDFour, cutoff)

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

diversity('Random', recomendationRANDOMFour, cutoff)
diversity('Skyline', recomendationSKYLINEFour, cutoff)
diversity('Popularity', recomendationPOPFour, cutoff)
diversity('Knn', recomendationKNNFour, cutoff)
diversity('Hybrid', recomendationHYBRIDFour, cutoff)

print('Coverage:')

cover('Random', recomendationRANDOMFour, cutoff)
cover('Skyline', recomendationSKYLINEFour, cutoff)
cover('Popularity', recomendationPOPFour, cutoff)
cover('Knn', recomendationKNNFour, cutoff)
cover('Hybrid', recomendationHYBRIDFour, cutoff)


# print('GOWALLA:\n')

# print('Precision con cutoff:', cutoff)

# # precision('Random', recomendationRANDOMGow, test_ny_Gow, cutoff)
# # precision('Skyline', recomendationSKYLINEGow, test_ny_Gow, cutoff)
# precision('Popularity', recomendationPOPGow, test_ny, cutoff)
# # precision('Knn', recomendationKNNGow, test_ny_Gow, cutoff)
# # precision('Hybrid', recomendationHYBRIDGow, test_ny_Gow, cutoff)

# print('Recall con cutoff:', cutoff)

# # recall('Random', recomendationRANDOMGow, test_ny_Gow, cutoff)
# # recall('Skyline', recomendationSKYLINEGow, test_ny_Gow, cutoff)
# recall('Popularity', recomendationPOPGow, test_ny, cutoff)
# # recall('Knn', recomendationKNNGow, test_ny_Gow, cutoff)
# # recall('Hybrid', recomendationHYBRIDGow, test_ny_Gow, cutoff)

# print('Agregate diversity con cutoff:', cutoff)

# # diversity('Random', recomendationRANDOMGow, cutoff)
# # diversity('Skyline', recomendationSKYLINEGow, cutoff)
# diversity('Popularity', recomendationPOPGow, cutoff)
# # diversity('Knn', recomendationKNNGow, cutoff)
# # diversity('Hybrid', recomendationHYBRIDGow, cutoff)