from cover import cover
from precision import precision
from recall import recall
from diversity import diversity
from expected_popularity import expected_popularity

# NEW YORK

# test_ny = '../recomendation/train_test/Gowalla/US_NewYork/US_NewYork_test.txt'
# train_ny_four = '../recomendation/train_test/Foursquare/US_NewYork/US_NewYork_train.txt'
# train_ny_gow = '../recomendation/train_test/Gowalla/US_NewYork/US_NewYork_train.txt'


# recomendationPOPGow = '../recomendation/users_recomendations/Gowalla/Popularity/NY_Top50_RepeatedScoreTrue.txt'
# recomendationPOPFour = '../recomendation/users_recomendations/Foursquare/Popularity/NY_Top50_RepeatedScoreTrue.txt'

# recomendationKNNGow = '../recomendation/users_recomendations/Gowalla/Knn/NY_Top50_Knn50.txt'
# recomendationKNNFour = '../recomendation/users_recomendations/Foursquare/Knn/NY_Top50_Knn50.txt'

# recomendationHYBRIDGow = '../recomendation/users_recomendations/Gowalla/Hybrid/NY_Top50_knn50.txt'
# recomendationHYBRIDFour = '../recomendation/users_recomendations/Foursquare/Hybrid/NY_Top50_knn50.txt'

# recomendationRANDOMGow = '../recomendation/users_recomendations/Gowalla/Random/NY_50.txt'
# recomendationRANDOMFour = '../recomendation/users_recomendations/Foursquare/Random/NY_50.txt'

# recomendationSKYLINEGow = '../recomendation/users_recomendations/Gowalla/Skyline/NY_Skyline.txt'
# recomendationSKYLINEFour = '../recomendation/users_recomendations/Foursquare/Skyline/NY_Skyline.txt'



# TOKYO

test_ny = '../recomendation/train_test/Gowalla/JP_Tokyo/test.txt'
train_ny_four = '../recomendation/train_test/Foursquare/JP_Tokyo/train.txt'
train_ny_gow = '../recomendation/train_test/Gowalla/JP_Tokyo/train.txt'


recomendationPOPGow = '../recomendation/users_recomendations/Gowalla/Popularity/TK_Top50_RepeatedScoreTrue.txt'
recomendationPOPFour = '../recomendation/users_recomendations/Foursquare/Popularity/TK_Top50_RepeatedScoreTrue.txt'



recomendationKNNGow50 = '../recomendation/users_recomendations/Gowalla/Knn/TK_Top50_Knn50.txt'
recomendationKNNFour50 = '../recomendation/users_recomendations/Foursquare/Knn/TK_Top50_Knn50.txt'

recomendationKNNGow5 = '../recomendation/users_recomendations/Gowalla/Knn/TK_Top50_Knn5.txt'
recomendationKNNFour5 = '../recomendation/users_recomendations/Foursquare/Knn/TK_Top50_Knn5.txt'

recomendationKNNGow100 = '../recomendation/users_recomendations/Gowalla/Knn/TK_Top50_Knn100.txt'
recomendationKNNFour100 = '../recomendation/users_recomendations/Foursquare/Knn/TK_Top50_Knn100.txt'



recomendationHYBRIDGow50 = '../recomendation/users_recomendations/Gowalla/Hybrid/TK_Top50_knn50.txt'
recomendationHYBRIDFour50 = '../recomendation/users_recomendations/Foursquare/Hybrid/TK_Top50_knn50.txt'

recomendationHYBRIDGow5 = '../recomendation/users_recomendations/Gowalla/Hybrid/TK_Top50_knn5.txt'
recomendationHYBRIDFour5 = '../recomendation/users_recomendations/Foursquare/Hybrid/TK_Top50_knn5.txt'

recomendationHYBRIDGow100 = '../recomendation/users_recomendations/Gowalla/Hybrid/TK_Top50_knn100.txt'
recomendationHYBRIDFour100 = '../recomendation/users_recomendations/Foursquare/Hybrid/TK_Top50_knn100.txt'

recomendationRANDOMGow = '../recomendation/users_recomendations/Gowalla/Random/TK_50.txt'
recomendationRANDOMFour = '../recomendation/users_recomendations/Foursquare/Random/TK_50.txt'

recomendationSKYLINEGow = '../recomendation/users_recomendations/Gowalla/Skyline/TK_Skyline.txt'
recomendationSKYLINEFour = '../recomendation/users_recomendations/Foursquare/Skyline/TK_Skyline.txt'


cutoff = 5

print('Precision:')

print(' Foursquare')

# precision('Random', recomendationRANDOMFour, test_ny, cutoff)
# precision('Skyline', recomendationSKYLINEFour, test_ny, cutoff)
# precision('Popularity', recomendationPOPFour, test_ny, cutoff)
precision('Knn5', recomendationKNNFour5, test_ny, cutoff)
precision('Knn50', recomendationKNNFour50, test_ny, cutoff)
precision('Knn100', recomendationKNNFour100, test_ny, cutoff)

print(' Gowalla:')

precision('Knn5', recomendationKNNGow5, test_ny, cutoff)
precision('Knn50', recomendationKNNGow50, test_ny, cutoff)
precision('Knn100', recomendationKNNGow100, test_ny, cutoff)

print(' Foursquare')
precision('Hybrid5', recomendationHYBRIDFour5, test_ny, cutoff)
precision('Hybrid50', recomendationHYBRIDFour50, test_ny, cutoff)
precision('Hybrid100', recomendationHYBRIDFour100, test_ny, cutoff)

print(' Gowalla:')

precision('Hybrid5', recomendationHYBRIDGow5, test_ny, cutoff)
precision('Hybrid50', recomendationHYBRIDGow50, test_ny, cutoff)
precision('Hybrid100', recomendationHYBRIDGow100, test_ny, cutoff)


# precision('Random', recomendationRANDOMGow, test_ny, cutoff)
# precision('Skyline', recomendationSKYLINEGow, test_ny, cutoff)
# precision('Popularity', recomendationPOPGow, test_ny, cutoff)
# precision('Knn', recomendationKNNGow5, test_ny, cutoff)
# precision('Knn', recomendationKNNGow50, test_ny, cutoff)
# precision('Knn', recomendationKNNGow100, test_ny, cutoff)
# precision('Hybrid', recomendationHYBRIDGow, test_ny, cutoff)



print('Recall:')

print(' Foursquare')

# recall('Random', recomendationRANDOMFour, test_ny, cutoff)
# recall('Skyline', recomendationSKYLINEFour, test_ny, cutoff)
# recall('Popularity', recomendationPOPFour, test_ny, cutoff)
recall('Knn5', recomendationKNNFour5, test_ny, cutoff)
recall('Knn50', recomendationKNNFour50, test_ny, cutoff)
recall('Knn100', recomendationKNNFour100, test_ny, cutoff)

print(' Gowalla:')
recall('Knn5', recomendationKNNGow5, test_ny, cutoff)
recall('Knn50', recomendationKNNGow50, test_ny, cutoff)
recall('Knn100', recomendationKNNGow100, test_ny, cutoff)

print(' Foursquare')
recall('Hybrid5', recomendationHYBRIDFour5, test_ny, cutoff)
recall('Hybrid50', recomendationHYBRIDFour50, test_ny, cutoff)
recall('Hybrid100', recomendationHYBRIDFour100, test_ny, cutoff)

print(' Gowalla:')

# recall('Random', recomendationRANDOMGow, test_ny, cutoff)
# recall('Skyline', recomendationSKYLINEGow, test_ny, cutoff)
# recall('Popularity', recomendationPOPGow, test_ny, cutoff)
# recall('Knn', recomendationKNNGow, test_ny, cutoff)
recall('Hybrid5', recomendationHYBRIDGow5, test_ny, cutoff)
recall('Hybrid50', recomendationHYBRIDGow50, test_ny, cutoff)
recall('Hybrid100', recomendationHYBRIDGow100, test_ny, cutoff)

# print('\n')

# print('Agregate diversity:')

# print(' Foursquare')

# diversity('Random', recomendationRANDOMFour)
# diversity('Skyline', recomendationSKYLINEFour)
# diversity('Popularity', recomendationPOPFour)
# diversity('Knn', recomendationKNNFour)
# diversity('Hybrid', recomendationHYBRIDFour)

# print(' Gowalla:')

# diversity('Random', recomendationRANDOMGow)
# diversity('Skyline', recomendationSKYLINEGow)
# diversity('Popularity', recomendationPOPGow)
# diversity('Knn', recomendationKNNGow)
# diversity('Hybrid', recomendationHYBRIDGow)

# print('\n')

# print('Coverage:')

# print(' Foursquare')

# cover('Random', recomendationRANDOMFour)
# cover('Skyline', recomendationSKYLINEFour)
# cover('Popularity', recomendationPOPFour)
# cover('Knn', recomendationKNNFour)
# cover('Hybrid', recomendationHYBRIDFour)

# print(' Gowalla:')

# cover('Random', recomendationRANDOMGow)
# cover('Skyline', recomendationSKYLINEGow)
# cover('Popularity', recomendationPOPGow)
# cover('Knn', recomendationKNNGow)
# cover('Hybrid', recomendationHYBRIDGow)

# print('\n')

# print('Expected popularity:')

# print(' Foursquare')

# expected_popularity('Random', recomendationRANDOMFour, test_ny, train_ny_four, cutoff)
# expected_popularity('Skyline', recomendationSKYLINEFour, test_ny, train_ny_four, cutoff)
# expected_popularity('Popularity', recomendationPOPFour, test_ny, train_ny_four, cutoff)
# expected_popularity('Knn', recomendationKNNFour, test_ny, train_ny_four, cutoff)
# expected_popularity('Hybrid', recomendationHYBRIDFour, test_ny, train_ny_four, cutoff)

# print(' Gowalla:')

# expected_popularity('Random', recomendationRANDOMGow, test_ny, train_ny_gow, cutoff)
# expected_popularity('Skyline', recomendationSKYLINEGow, test_ny, train_ny_gow, cutoff)
# expected_popularity('Popularity', recomendationPOPGow, test_ny, train_ny_gow, cutoff)
# expected_popularity('Knn', recomendationKNNGow, test_ny, train_ny_gow, cutoff)
# expected_popularity('Hybrid', recomendationHYBRIDGow, test_ny, train_ny_gow, cutoff)
