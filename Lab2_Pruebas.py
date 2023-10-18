#%%

import pandas as pd
import folium
import random
from branca.element import Template, MacroElement

data = pd.read_csv("lista.csv")

coordenadas_aeropuertos = {}
for index, row in data.iterrows():
    origen = (row['Source Airport Latitude'], row['Source Airport Longitude'])
    destino = (row['Destination Airport Latitude'], row['Destination Airport Longitude'])

    coordenadas_aeropuertos[row['Source Airport Code']] = origen
    coordenadas_aeropuertos[row['Destination Airport Code']] = destino

initial_location = coordenadas_aeropuertos[list(coordenadas_aeropuertos.keys())[0]]
mapa = folium.Map()

airport_codes = list(coordenadas_aeropuertos.keys())

# Agregar todos los marcadores al mapa en un FeatureGroup
todos_los_aeropuertos = folium.FeatureGroup(name="Todos los aeropuertos")
for airport_code in airport_codes:
    marker = folium.Marker(
        location=coordenadas_aeropuertos[airport_code],
        popup=airport_code,
    )
    todos_los_aeropuertos.add_child(marker)

#mapa.add_child(todos_los_aeropuertos)

# Crear un panel lateral con botones
template = """
{% macro html(this, kwargs) %}

<div id="mydiv" style="position: fixed; bottom: 60px; left: 60px; width: 250px; height: 140px; z-index:9999; font-size:14px;">
    <input type="button" value="Mostrar todos los aeropuertos" onclick="showAllAirports();">
    <input type="button" value="Mostrar aeropuerto específico" onclick="showSpecificAirport();">
    <input type="button" value="Mostrar  segundo  aeropuerto" onclick="showRandomAirport();">
</div>

<script>
function showAllAirports() {
    // Aquí va tu código para mostrar todos los aeropuertos
}

function showSpecificAirport() {
    // Aquí va tu código para mostrar un aeropuerto específico
}

function showRandomAirport() {
    // Aquí va tu código para mostrar un aeropuerto aleatorio
}
</script>

{% endmacro %}
"""

macro = MacroElement()
macro._template = Template(template)

mapa.get_root().add_child(macro)

# Guardar el mapa en un archivo HTML
mapa.save("mapa.html")



# %%
