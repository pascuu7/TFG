from knn import knn
from rand import rand
from popularity import popularity
from hybrid import hybrid
from skyline import skyline
import sys

if __name__ == "__main__":
    train_f = 'train_test/Foursquare/' + sys.argv[1] + '/' + sys.argv[1] + '_train.txt'
    train_g = 'train_test/Gowalla/' + sys.argv[1] + '/' + sys.argv[1] + '_train.txt'
    test = 'train_test/Gowalla/' + sys.argv[1] + '/' + sys.argv[1] + '_test.txt'

    # guardamos en pre el prefijo del país que se indique
    if sys.argv[1] == "US_SanFrancisco":
        pre = 'SF'

    elif sys.argv[1] == "US_NewYork":
        pre = 'NY'

    else:
        pre = 'TK'

    # Recomendador de popularidad

    fout_false_pop_f = 'users_recomendations/Foursquare/Popularity/' + pre + '_Top50_RepeatedScoreFalse.txt'
    popularity(train_f, test, out=fout_false_pop_f)

    fout_false_pop_g = 'users_recomendations/Gowalla/Popularity/' + pre + '_Top50_RepeatedScoreFalse.txt'
    popularity(train_g, test, out=fout_false_pop_g)


    # Recomendador de vecinos próximos

    fout_knn_f = 'users_recomendations/Foursquare/Knn/' + pre + '_Top50_Knn100.txt'
    knn(train_f, test, 100, out=fout_knn_f)

    fout_knn_g = 'users_recomendations/Gowalla/Knn/' + pre + '_Top50_Knn100.txt'
    knn(train_g, test, 100, out=fout_knn_g)


    # Recomendador híbrido

    poi_file = '../dataset/Foursquare/POI_city.txt'

    fout_hybrid_f = 'users_recomendations/Foursquare/Hybrid/' + pre + '_Top50_knn100.txt'
    hybrid(poi_file, train_f, test, fout_hybrid_f, 100)

    fout_hybrid_g = 'users_recomendations/Gowalla/Hybrid/' + pre + '_Top50_knn100.txt'
    hybrid(poi_file, train_g, test, fout_hybrid_g, 100)

    # Recomendador Random

    fout_random_f = 'users_recomendations/Foursquare/Random/' + pre + '_50.txt'
    rand(train_f, test, fout_random_f)

    fout_random_g = 'users_recomendations/Gowalla/Random/' + pre + '_50.txt'
    rand(train_g, test, fout_random_g)

    # Recomendador Skyline

    fout_skyline_f = 'users_recomendations/Foursquare/Skyline/' + pre + '_Skyline.txt'
    skyline(train_f, test, fout_skyline_f)

    fout_skyline_g = 'users_recomendations/Gowalla/Skyline/' + pre + '_Skyline.txt'
    skyline(train_g, test, fout_skyline_g)