from cover import cover
from precision import precision
from recall import recall
from diversity import diversity
from expected_popularity import expected_popularity

import sys

if __name__ == "__main__":

    test = '../recomendation/train_test/Gowalla/' + sys.argv[1] + '/' + sys.argv[1] + '_test.txt'
    train_four = '../recomendation/train_test/Foursquare/' + sys.argv[1] + '/' + sys.argv[1] + '_train.txt'
    train_gow = '../recomendation/train_test/Gowalla/' + sys.argv[1] + '/' + sys.argv[1] + '_train.txt'

    if sys.argv[1] == "US_SanFrancisco":
        pre = 'SF'

    elif sys.argv[1] == "US_NewYork":
        pre = 'NY'

    else:
        pre = 'TK'

    recomendationPOPGow = '../recomendation/users_recomendations/Gowalla/Popularity/' + pre + '_Top50_RepeatedScore' + sys.argv[2] + '.txt'
    recomendationPOPFour = '../recomendation/users_recomendations/Foursquare/Popularity/' + pre + '_Top50_RepeatedScore' + sys.argv[2] + '.txt'

    recomendationKNNGow = '../recomendation/users_recomendations/Gowalla/Knn/' + pre + '_Top50_Knn' + sys.argv[3] + '.txt'
    recomendationKNNFour = '../recomendation/users_recomendations/Foursquare/Knn/' + pre + '_Top50_Knn' + sys.argv[3] + '.txt'

    recomendationHYBRIDGow = '../recomendation/users_recomendations/Gowalla/Hybrid/' + pre + '_Top50_knn' + sys.argv[3] + '.txt'
    recomendationHYBRIDFour = '../recomendation/users_recomendations/Foursquare/Hybrid/' + pre + '_Top50_knn' + sys.argv[3] + '.txt'

    recomendationRANDOMGow = '../recomendation/users_recomendations/Gowalla/Random/' + pre + '_50.txt'
    recomendationRANDOMFour = '../recomendation/users_recomendations/Foursquare/Random/' + pre + '_50.txt'

    recomendationSKYLINEGow = '../recomendation/users_recomendations/Gowalla/Skyline/' + pre + '_Skyline.txt'
    recomendationSKYLINEFour = '../recomendation/users_recomendations/Foursquare/Skyline/' + pre + '_Skyline.txt'


    cutoff = int(sys.argv[4])

    print('Precision:')

    print(' Foursquare')

    precision('Random', recomendationRANDOMFour, test, cutoff)
    precision('Skyline', recomendationSKYLINEFour, test, cutoff)
    precision('Popularity', recomendationPOPFour, test, cutoff)
    precision('Knn', recomendationKNNFour, test, cutoff)
    precision('Hybrid', recomendationHYBRIDFour, test, cutoff)

    print(' Gowalla:')

    precision('Random', recomendationRANDOMGow, test, cutoff)
    precision('Skyline', recomendationSKYLINEGow, test, cutoff)
    precision('Popularity', recomendationPOPGow, test, cutoff)
    precision('Knn', recomendationKNNGow, test, cutoff)
    precision('Hybrid', recomendationHYBRIDGow, test, cutoff)

    print('\n')


    print('Recall:')

    print(' Foursquare')

    recall('Random', recomendationRANDOMFour, test, cutoff)
    recall('Skyline', recomendationSKYLINEFour, test, cutoff)
    recall('Popularity', recomendationPOPFour, test, cutoff)
    recall('Knn', recomendationKNNFour, test, cutoff)
    recall('Hybrid', recomendationHYBRIDFour, test, cutoff)

    print(' Gowalla:')

    recall('Random', recomendationRANDOMGow, test, cutoff)
    recall('Skyline', recomendationSKYLINEGow, test, cutoff)
    recall('Popularity', recomendationPOPGow, test, cutoff)
    recall('Knn', recomendationKNNGow, test, cutoff)
    recall('Hybrid', recomendationHYBRIDGow, test, cutoff)

    print('\n')


    print('Expected popularity:')

    print(' Foursquare')

    expected_popularity('Random', recomendationRANDOMFour, test, train_four, cutoff)
    expected_popularity('Skyline', recomendationSKYLINEFour, test, train_four, cutoff)
    expected_popularity('Popularity', recomendationPOPFour, test, train_four, cutoff)
    expected_popularity('Knn', recomendationKNNFour, test, train_four, cutoff)
    expected_popularity('Hybrid', recomendationHYBRIDFour, test, train_four, cutoff)

    print(' Gowalla:')

    expected_popularity('Random', recomendationRANDOMGow, test, train_four, cutoff)
    expected_popularity('Skyline', recomendationSKYLINEGow, test, train_four, cutoff)
    expected_popularity('Popularity', recomendationPOPGow, test, train_four, cutoff)
    expected_popularity('Knn', recomendationKNNGow, test, train_four, cutoff)
    expected_popularity('Hybrid', recomendationHYBRIDGow, test, train_four, cutoff)

    print('\n')


    print('Aggregate diversity:')

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
