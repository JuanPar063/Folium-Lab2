# Folium Lab 2 - Mapa Interactivo de Aeropuertos con Dijkstra

Laboratorio de la materia **Estructura de Datos** que implementa el algoritmo de Dijkstra sobre un grafo de aeropuertos, visualizando las rutas optimas en un mapa interactivo con la libreria Folium.

## Descripcion

Este proyecto carga un dataset de vuelos entre aeropuertos, construye un grafo donde los aeropuertos son nodos y las rutas de vuelo son aristas ponderadas, y aplica el **algoritmo de Dijkstra** para encontrar los caminos mas cortos entre distintos aeropuertos. Los resultados se visualizan en un mapa interactivo generado con [Folium](https://python-visualization.github.io/folium/), basado en Leaflet.js.

## Estructura del Proyecto

```
Folium-Lab2/
├── Lab2_Map.py          # Script principal: carga datos, construye el mapa interactivo
├── Lab2_Pruebas.py      # Script de pruebas del algoritmo de Dijkstra
├── flights_clean.csv    # Dataset limpio de vuelos entre aeropuertos
├── flights_final.csv    # Dataset final de vuelos utilizado en el proyecto
└── mapa.html            # Mapa interactivo generado (output)
```

## Tecnologias Utilizadas

- **Python** - Lenguaje de programacion principal
- **Pandas** - Lectura y manipulacion del dataset CSV
- **Folium** - Generacion de mapas interactivos (basado en Leaflet.js)
- **HTML** - Visualizacion del mapa resultante en el navegador

## Algoritmo Implementado

### Dijkstra

Algoritmo de busqueda del camino mas corto en grafos ponderados con pesos no negativos. En este proyecto:

- Los **nodos** son aeropuertos (identificados por codigo IATA).
- Las **aristas** son rutas de vuelo con su distancia o costo asociado.
- Se calcula la ruta optima entre aeropuertos de origen y destino.

## Dataset

Los archivos CSV contienen informacion de vuelos con las siguientes columnas:

| Columna | Descripcion |
|---|---|
| Source Airport Code | Codigo IATA del aeropuerto origen |
| Source Airport Name | Nombre del aeropuerto origen |
| Source Airport City | Ciudad del aeropuerto origen |
| Source Airport Country | Pais del aeropuerto origen |
| Source Airport Latitude/Longitude | Coordenadas geograficas del origen |
| Destination Airport Code | Codigo IATA del aeropuerto destino |
| Destination Airport Latitude/Longitude | Coordenadas geograficas del destino |

## Instalacion y Ejecucion

### Requisitos previos

```bash
pip install pandas folium
```

### Ejecutar el mapa

```bash
python Lab2_Map.py
```

Esto generara el archivo `mapa.html` con el mapa interactivo. Abrelo en tu navegador.

### Ejecutar las pruebas

```bash
python Lab2_Pruebas.py
```

## Caracteristicas del Mapa

- Marcadores en cada aeropuerto con su codigo IATA como popup
- Visualizacion de rutas entre aeropuertos
- Control de capas (LayerControl)
- Mapa centrado en el primer aeropuerto del dataset
- Interactividad: click en marcadores para ver detalles del aeropuerto

## Autor

Juan Sebastian Pardo Anzola - [@JuanPar063](https://github.com/JuanPar063)
