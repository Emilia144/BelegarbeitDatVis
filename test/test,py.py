import geojson
import folium

# Funktion zum Laden der GeoJSON-Datei
def load_geojson(file_path):
    with open(file_path) as f:
        data = geojson.load(f)
    return data

# Funktion zum Erstellen einer Folium-Karte und Hinzufügen des GeoJSON-Layers
def create_map(geojson_data):
    # Extrahieren Sie den Mittelpunkt des ersten Punktes, um die Karte zu zentrieren
    feature = geojson_data['features'][0]
    geometry = feature['geometry']
    coordinates = geometry['coordinates']
    center = [coordinates[1], coordinates[0]]  # Lat, Lon

    # Erstellen Sie eine Folium-Karte
    m = folium.Map(location=center, zoom_start=13)

    # Fügen Sie jeden Punkt als Marker zur Karte hinzu
    for feature in geojson_data['features']:
        geometry = feature['geometry']
        if geometry['type'] == 'Point':
            coordinates = geometry['coordinates']
            folium.Marker(location=[coordinates[1], coordinates[0]]).add_to(m)

    return m

# Pfad zur GeoJSON-Datei
geojson_file_path = 'capitals.geojson'

# Laden der GeoJSON-Datei
geojson_data = load_geojson(geojson_file_path)

# Erstellen der Karte mit dem GeoJSON-Layer
mymap = create_map(geojson_data)

# Speichern der Karte in einer HTML-Datei
mymap.save('map.html')


