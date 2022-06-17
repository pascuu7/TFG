# TFG

Framework que trabaja con con los datos de las aplicaciones Foursquare y Gowalla para efectuar recomendaciones y evaluarlas.

# Intstrucciones de ejecución

 Crear las carpetas necesarias para la ejecución: 
1. `python3 setup.py`

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

Recomendaciones (las ciudades disponibles son US_NewYork, US_SanFrancisco y JP_Tokyo):
1. `cd ../recomendation/`
2. `python3 recommend.py` (recomienda con los parámetros estudiados, knn = 100 y sin elementos repetidos en popularidad).
3. `python3 popularity.py ciudad False` (se puede cambiar False a True para recomendar con elementos repetidos).
4. `python3 knn.py ciudad 100` (el número de vecinos puede ser el que el usuario desee, cuanto más alto más tarda la ejecución).
5. `python3 hybrid.py ciudad 100` (el número de vecinos puede ser el que el usuario desee, el tiempo es el mismo para cualquiera pero tiene que estar antes hecha la recomendación knn para esos vecinos).
6. `python3 rand.py ciudad`
7. `python3 skyline.py ciudad`

Evaluación:
1. `cd ../evaluation/`
2. `python3 evaluate.py`



