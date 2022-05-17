from precision import precision
from recall import recall
from diversity import diversity

test_ny = '../recomendation/train_test/US_NewYork/US_NewYork_test.txt'
recomendationPOP = '../recomendation/users_recomendations/Popularity/NY_Top50_RepeatedScoreTrue.txt'
recomendationKNN = '../recomendation/users_recomendations/Knn/NY_Top50_Knn5.txt'
recomendationHYBRID = '../recomendation/users_recomendations/Hybrid/NY_Top50_knn50.txt'
recomendationRANDOM = '../recomendation/users_recomendations/Random/NY_50.txt'
recomendationSKYLINE = '../recomendation/users_recomendations/Skyline/NY_Skyline.txt'

cutoff = 50

# print('Precision con cutoff:', cutoff)

# # precision('Random', recomendationRANDOM, test_ny, cutoff)
# # precision('Skyline', recomendationSKYLINE, test_ny, cutoff)
# precision('Popularity', recomendationPOP, test_ny, cutoff)
# precision('Knn', recomendationKNN, test_ny, cutoff)
# precision('Hybrid', recomendationHYBRID, test_ny, cutoff)

# print('Recall con cutoff:', cutoff)

# recall('Random', recomendationRANDOM, test_ny, cutoff)
# recall('Skyline', recomendationSKYLINE, test_ny, cutoff)
# recall('Popularity', recomendationPOP, test_ny, cutoff)
# recall('Knn', recomendationKNN, test_ny, cutoff)
# recall('Hybrid', recomendationHYBRID, test_ny, cutoff)

print('Agregate diversity con cutoff:', cutoff)

# diversity('Random', recomendationRANDOM, cutoff)
# diversity('Skyline', recomendationSKYLINE, cutoff)
diversity('Popularity', recomendationPOP, cutoff)
# diversity('Knn', recomendationKNN, cutoff)
# diversity('Hybrid', recomendationHYBRID, cutoff)

