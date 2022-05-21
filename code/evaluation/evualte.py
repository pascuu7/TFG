from precision import precision
from recall import recall
from diversity import diversity

test_ny_Gow = '../recomendation/train_test/Gowalla/US_NewYork/US_NewYork_test.txt'
test_ny_Four = '../recomendation/train_test/Foursquare/US_NewYork/US_NewYork_test.txt'


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


print('FOURSQUARE:\n')

print('Precision con cutoff:', cutoff)

precision('Random', recomendationRANDOMFour, test_ny_Four, cutoff)
precision('Skyline', recomendationSKYLINEFour, test_ny_Four, cutoff)
precision('Popularity', recomendationPOPFour, test_ny_Four, cutoff)
precision('Knn', recomendationKNNFour, test_ny_Four, cutoff)
precision('Hybrid', recomendationHYBRIDFour, test_ny_Four, cutoff)

print('Recall con cutoff:', cutoff)

recall('Random', recomendationRANDOMFour, test_ny_Four, cutoff)
recall('Skyline', recomendationSKYLINEFour, test_ny_Four, cutoff)
recall('Popularity', recomendationPOPFour, test_ny_Four, cutoff)
recall('Knn', recomendationKNNFour, test_ny_Four, cutoff)
recall('Hybrid', recomendationHYBRIDFour, test_ny_Four, cutoff)

print('Agregate diversity con cutoff:', cutoff)

diversity('Random', recomendationRANDOMFour, cutoff)
diversity('Skyline', recomendationSKYLINEFour, cutoff)
diversity('Popularity', recomendationPOPFour, cutoff)
diversity('Knn', recomendationKNNFour, cutoff)
diversity('Hybrid', recomendationHYBRIDFour, cutoff)



print('GOWALLA:\n')

print('Precision con cutoff:', cutoff)

precision('Random', recomendationRANDOMGow, test_ny_Gow, cutoff)
precision('Skyline', recomendationSKYLINEGow, test_ny_Gow, cutoff)
precision('Popularity', recomendationPOPGow, test_ny_Gow, cutoff)
precision('Knn', recomendationKNNGow, test_ny_Gow, cutoff)
precision('Hybrid', recomendationHYBRIDGow, test_ny_Gow, cutoff)

print('Recall con cutoff:', cutoff)

recall('Random', recomendationRANDOMGow, test_ny_Gow, cutoff)
recall('Skyline', recomendationSKYLINEGow, test_ny_Gow, cutoff)
recall('Popularity', recomendationPOPGow, test_ny_Gow, cutoff)
recall('Knn', recomendationKNNGow, test_ny_Gow, cutoff)
recall('Hybrid', recomendationHYBRIDGow, test_ny_Gow, cutoff)

print('Agregate diversity con cutoff:', cutoff)

diversity('Random', recomendationRANDOMGow, cutoff)
diversity('Skyline', recomendationSKYLINEGow, cutoff)
diversity('Popularity', recomendationPOPGow, cutoff)
diversity('Knn', recomendationKNNGow, cutoff)
diversity('Hybrid', recomendationHYBRIDGow, cutoff)

