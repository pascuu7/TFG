# TFG

Framework que trabaja con con los datos de las aplicaciones Foursquare y Gowalla para efectuar recomendaciones y evaluarlas.

# Intstrucciones de ejecución

Crear las carpetas necesarias para la ejecución: 
1. `python3 setup.py`

Descargar el dataset de las aplicaciones Foursquare y Gowalla:
1. Descargar el dataset que contiene (3.Global-scale Check-in Dataset) en la URL https://sites.google.com/site/yangdingqi/home/foursquare-dataset y extraer los ficheros en el directorio dataset/Foursquare/dataset/.
2. Descargar el dataset que contiene (loc-gowalla_totalCheckins.txt.gz) en la URL https://snap.stanford.edu/data/loc-gowalla.html y extraer el fichero en el directorio dataset/Gowalla.

Preparar el dataset:
1. `cd dataset/Foursquare/`
2. `python3 cities.py`
3. `python3 checkins.py`
4. `cd ../Gowalla/`
5. `python3 poi_check.py`
6. `cd ../coincidencias/`
7. `python3 coincidencias_pois.py`
8. `python3 coincidencias_users.py`
9. `cd ../`
10. `python3 all_checkins.py`
11. `python3 rating.py`
12. `cd Foursquare/`
13. `python3 rating.py`
14. `cd ../`
15. `python3 train_test.py`

Recomendaciones (las ciudades disponibles son US_NewYork, US_SanFrancisco y JP_Tokyo) hay dos opciones.
Recomendar con los parámetros estudiados, knn = 100 y sin elementos repetidos en popularidad):
1. `cd ../recomendation/`
2. `python3 recommend.py ciudad` donde ciudad corresponde con las 3 ciudades indicadas arriba.

Recomendar cada algoritmo por separando escogiendo los parámetros:
1. `cd ../recomendation/`
2. `python3 popularity.py ciudad repeated` (repeated puede se False o True dependiendo de si se quiere recomendar con elementos repetidos).
3. `python3 knn.py ciudad knn` (el número de vecinos o knn puede ser el que el usuario desee, cuanto más alto más tarda la ejecución).
4. `python3 hybrid.py ciudad knn` (el número de vecinos o knn puede ser el que el usuario desee, el tiempo es el mismo para cualquiera pero tiene que estar antes hecha la recomendación knn para esos vecinos).
5. `python3 rand.py ciudad`
6. `python3 skyline.py ciudad`

Evaluación:
1. `cd ../evaluation/`
2. `python3 evaluate.py ciudad repeated knn` (ciudad, repeated y knn es lo mismo que se ha indicado en la recomenación)



