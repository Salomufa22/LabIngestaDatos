import sqlite3
import pandas as pd

# Creación de la DB y carga de datos.
conn = sqlite3.connect('IngestaDatos.db')

df1 = pd.read_csv('cities.csv')
df2 = pd.read_csv('ConAir.csv')

df1.to_sql('Cities', conn, if_exists='replace', index=False)
df2.to_sql('ConAir', conn, if_exists='replace', index=False)

# Query para verificar si las ciudades más pobladas tienen la peor calidad del aire.
query = '''
SELECT Cities.City, Cities."Total population", ConAir.CO, ConAir.NO2, ConAir.O3, ConAir."PM2.5", ConAir.PM10
FROM Cities
JOIN ConAir ON ConAir.City = Cities.City
ORDER BY Cities."Total population" DESC
LIMIT 0, 10;
'''
result_df1 = pd.read_sql_query(query, conn)
result_df1.to_csv("CalidadAireCiudad.csv")
#print(result_df1)
conn.close()