# Análisis de calidad del aire y datos demográficos

## Introducción
Este proyecto se enfoca en analizar la calidad del aire en ciudades de los Estados Unidos y su relación con los datos demográficos de estas ciudades. El objetivo principal es determinar si existe alguna correlación entre la densidad de población y la calidad del aire. Para esto, se utilizaron datos demográficos obtenidos de un archivo CSV y datos de calidad del aire obtenidos a través de una API.

## Proceso

### 1. Carga de datos demográficos
Se cargaron los datos demográficos de las ciudades de Estados Unidos desde el archivo CSV utilizando la biblioteca pandas en Python.

### 2. Obtención de datos de calidad del aire
Los datos de calidad del aire para cada ciudad se obtuvieron utilizando la API de https://api-ninjas.com/api/airquality.

### 3. Limpieza de datos demográficos
Se realizaron diversas operaciones de limpieza, incluida la eliminación de columnas innecesarias y la eliminación de filas duplicadas.

### 4. Creación de la base de datos
Se creó una base de datos en SQLite y se cargaron las tablas de datos demográficos y calidad del aire en la base de datos.

### 5. Análisis de datos
Se realizaron operaciones de unión y agregación en la base de datos utilizando consultas SQL para verificar si las ciudades más pobladas tienen peor calidad del aire.

### 6. Query para verificar si las ciudades más pobladas tienen la peor calidad del aire.
```
query = ''' 
SELECT Cities.City, Cities."Total population", ConAir.CO, ConAir.NO2, ConAir.O3, ConAir."PM2.5", ConAir.PM10
FROM Cities
JOIN ConAir ON ConAir.City = Cities.City
ORDER BY Cities."Total population" DESC
LIMIT 0, 10;
'''
```
## Resultados
Los resultados revelaron que, contrariamente a la expectativa, Los Ángeles, aunque no es la ciudad más poblada, presenta una peor calidad del aire en términos de concentración de CO, NO2, O3, PM2.5 y PM10 en comparación con Nueva York, que es la ciudad más poblada. Por lo tanto, los datos no respaldan la afirmación de que las ciudades más pobladas tienen necesariamente la peor calidad del aire. Para obtener información detallada, consulta el archivo 'CalidadAireCiudad.csv'.

## Archivos adjuntos
- El archivo 'CalidadAireCiudad.csv' contiene los  10 primeros resultados completos del análisis de calidad del aire.
- El archivo de base de datos SQLite 'IngestaDatos.db' contiene las tablas de datos demográficos y calidad del aire utilizadas en el análisis.

