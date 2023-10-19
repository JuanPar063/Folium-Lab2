#%%

import pandas as pd
import networkx as nx
from geopy.distance import geodesic

# Cargar el dataset
data = pd.read_csv("flights_final.csv")

# Obtener los códigos únicos de aeropuertos
codigos_aeropuertos_unicos_Source = data['Source Airport Code']
codigos_aeropuertos_unicos_Destination = data['Destination Airport Code']

# Inicializar un nuevo DataFrame vacío
nuevo_data = pd.DataFrame(columns=data.columns)
multilista = []
filas_cumplen = []

# Crear un grafo completo
G = nx.Graph()

# Iterar a través de las filas del DataFrame
for index, row in data.iterrows():
    valor1 = row['Source Airport Code']
    valor2 = row['Destination Airport Code']
    
    # Asegurarte de que los dos valores no sean iguales a los de otra sublista
    if (valor1, valor2) not in multilista and (valor2, valor1) not in multilista:
        filas_cumplen.append(row)
        multilista.append((valor1, valor2))

cantidad_de_sublistas = sum(1 for sublista in multilista if len(sublista) == 2)

print("Cantidad de sublistas con exactamente dos elementos:", cantidad_de_sublistas)
nuevo_data = pd.DataFrame(filas_cumplen)

nuevo_data.to_csv("flights_clean.csv", index=False)

nuevo_data

# %%
