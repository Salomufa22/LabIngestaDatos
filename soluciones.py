import pandas as pd
import requests
from typing import Set

def ej_1_cargar_datos_demograficos() -> pd.DataFrame:
    url = "https://public.opendatasoft.com/explore/dataset/us-cities-demographics/download/?format=csv&timezone=Europe/Berlin&lang=en&use_labels_for_header=true&csv_separator=%3B"
    data = pd.read_csv(url, sep=';')
    data = data.drop(['Race', 'Count', 'Number of Veterans'], axis=1) #Eliminar las columnas: Race, Count y Number of Veterans.
    data.drop_duplicates(inplace=True) #Eliminar las filas duplicadas 
    data.to_csv("cities.csv")
    return data

def ej_2_cargar_calidad_aire(ciudades: Set[str]) -> None:
    datos = pd.DataFrame({"City" : [],
                        "CO" : [],
                        "NO2" : [],
                        "O3" : [],
                        "SO2" : [],
                        "PM2.5" : [],
                        "PM10" : [] 
    })

    for ciudad in ciudades:
        api_url = 'https://api.api-ninjas.com/v1/airquality?city={}'.format(ciudad)
        response = requests.get(api_url, headers={'X-Api-Key': 'r8GQ/aUVyH0TezlLwmdE2w==rEH4c80WSCsQaOQs'})
        if response.status_code == requests.codes.ok:
            contenido = response.json()
            filaParaDataframe(datos, ciudad, contenido)
        else:
            print("Error:", response.status_code, response.text)
        
        # print(f" {ciudad} Done")
    
    print(datos)
    datos.to_csv("ConAir.csv")
    return datos

def filaParaDataframe(data, ciudad, content):

    newRow = [ciudad,
            content["CO"]["concentration"],
            content["NO2"]["concentration"],
            content["O3"]["concentration"],
            content["SO2"]["concentration"],
            content["PM2.5"]["concentration"],
            content["PM10"]["concentration"]
    ]
    data.loc[len(data.index)] = newRow




#data = ej_1_cargar_datos_demograficos()
#cities = data['City']
#cities = set(cities)
#ej_2_cargar_calidad_aire(cities)

#Por cada ciudad:
# Solicitud a API
# Con respuesta, obtener concentration
# Almacenar en tabla de dimensiones

