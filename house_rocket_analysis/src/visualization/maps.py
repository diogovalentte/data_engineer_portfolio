from folium.plugins import MarkerCluster
import geopandas
import folium
import plotly_express as px
import sys

sys.path.append('../../src/')  # Add folder "src" as a package path


def houses_map(data):
    """: data: renamed houses or filtered data"""

    map_density = folium.Map(location=[
        data['Latitude'].mean(),
        data['Longitude'].mean()],
        default_zoom_start=20)

    marker_cluster = MarkerCluster().add_to(map_density)

    for name, row in data.iterrows():
        folium.Marker([row['Latitude'], row['Longitude']],
                      popup='ID: {}, Price: {}, Year Built: {}, ZipCode: {}'.format(row['ID'], row['Price'], row['Year Built'], row['ZipCode'])).add_to(marker_cluster)

    return map_density


def price_per_region(data):
    """: data: renamed houses"""

    # Load geofile
    url = 'https://opendata.arcgis.com/datasets/83fc2e72903343aabff6de8cb445b81c_2.geojson'

    geofile = geopandas.read_file(url)

    # Group the avarage price per ZipCode
    ids_per_zipcode = data[['Price', 'ZipCode']].groupby(
        'ZipCode').mean().reset_index()

    geofile = geofile[geofile['ZIP'].isin(ids_per_zipcode['ZipCode'].tolist())]

    # Create the map
    map_price_zipcode = folium.Map(location=[
        data['Latitude'].mean(),
        data['Longitude'].mean()],
        default_zoom_start=19)

    map_price_zipcode.choropleth(data=ids_per_zipcode,
                                 geo_data=geofile,
                                 columns=['ZipCode', 'Price'],
                                 key_on='feature.properties.ZIP',
                                 fill_color='YlOrRd',
                                 fill_opacity=0.7,
                                 line_opacity=-0.2,
                                 legend_name='AVG Price Map'
                                 )

    return map_price_zipcode
