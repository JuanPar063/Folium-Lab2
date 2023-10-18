#%%
import pandas as pd
import folium
from folium.plugins import FloatImage


mapa = folium.Map()


# Guardar el DataFrame sin duplicados en un nuevo archivo CSV
data = pd.read_csv("lista.csv")



lista_categorias = ["code", "name", "city", "country", "latitud",
                    "longitud", "code_final", "name_final", "city_final",
                    "country_final", "latitud_final", "longitud_final"]
# creamos listas de los elementos de las columnas
code = data['Source Airport Code'].tolist()
name = data['Source Airport Name'].tolist()
city = data['Source Airport City'].tolist()
country = data['Source Airport Country'].tolist()
latitud = data['Source Airport Latitude'].tolist()
longitud = data['Source Airport Longitude'].tolist()
code_final = data['Destination Airport Code'].tolist()
name_final = data['Destination Airport Name'].tolist()
city_final = data['Destination Airport City'].tolist()
country_final = data['Destination Airport Country'].tolist()
latitud_final = data['Destination Airport Latitude'].tolist()
longitud_final = data['Destination Airport Longitude'].tolist()

data

coordenadas_aeropuertos = {}

for index, row in data.iterrows():
    origen = (row['Source Airport Latitude'], row['Source Airport Longitude'])
    destino = (row['Destination Airport Latitude'], row['Destination Airport Longitude'])

    coordenadas_aeropuertos[row['Source Airport Code']] = origen
    coordenadas_aeropuertos[row['Destination Airport Code']] = destino


# Definir una acción personalizada para ejecutar cuando se hace clic en un marcador
def on_marker_click(e):
    print(f"Marcador clicado: {e.target.get_popup().get_text()}")

# Crear un mapa centrado en una ubicación
initial_location = coordenadas_aeropuertos[list(coordenadas_aeropuertos.keys())[0]]
mapa = folium.Map(location=initial_location, zoom_start=6)

# Iterar sobre las coordenadas de los aeropuertos y agregar marcadores con acciones personalizadas
for airport_code, coordinates in coordenadas_aeropuertos.items():
    marker = folium.Marker(
        location=coordinates,
        popup=airport_code,
    )
    
    # Agregar la acción personalizada al marcador
    marker.add_child(folium.ClickForMarker(popup=f"Aeropuerto {airport_code}"))
    
    # Agregar el marcador al mapa
    marker.add_to(mapa)

##
# Agregar un control de radio para seleccionar la opción
folium.LayerControl().add_to(mapa)

# Crear un grupo de capas para las opciones
opciones = folium.FeatureGroup(name='Opciones')

# Agregar los botones de selección de opción
folium.MacroElement().add_to(opciones)

# Agregar las opciones al mapa
opciones.add_to(mapa)

# Agregar un botón flotante con desglose
url = ('https://raw.githubusercontent.com/....')  # URL de la imagen del botón
FloatImage(url, bottom=5, left=85).add_to(mapa)

# Agregar JavaScript para la funcionalidad del desglose
mapa.get_root().header.add_child(folium.Element("""
    <script>
    // Aquí va tu código JavaScript para el desglose del botón
    </script>
"""))
##
# Guardar el mapa en un archivo HTML
mapa.save("mapa.html")

# Mostrar el mapa en el navegador
mapa


#%%
