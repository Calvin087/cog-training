import folium
import csv
from bokeh.io import output_file, show
from bokeh.models import GMapPlot, GMapOptions, ColumnarDataSource, Circle, Range1d, PanTool, WheelZoomTool, BoxSelectTool

hello2 = folium.Map()
fghello = folium.FeatureGroup()

for lat, lon in zip(lats, lons):
    fghello.add_child(folium.CircleMarker(location = [lat, lon], fill = True))

hello2.add_child(fghello)

#------------------

lats = []
longs = []
# need floating point numbers.


with open('countries.csv') as f:
    # just opening the data
    file = csv.reader(f)

    for ab, lat,long,name in list(file)[1:]:

        lats.append(float(lat))
        longs.append(float(long))

map_options = GMapOptions(lat=0, lng=0, zoom=3)
# Start lat and lon for the map render

plot = GMapPlot(x_range = Range1d(), y_range = Range1d(), map_options=map_options)
# passing in ranges to start the plot

plot.title.text = 'The Example Plot'
# Text title if you want.

plot.api_key = input('Put Google API key here: ')
# key needed from Google dev / Javascript page is the same key

source = ColumnarDataSource(data=dict(lat=lats, lon=longs))
# setting the source for the data

circle = Circle(x='lon', y='lat', size=15, fill_color='red', fill_alpha=0.6)
# These are the red circles that are floating over the map

plot.add_glyph(source, circle)
# Matching up source with cirlces

plot.add_tools(PanTool(), WheelZoomTool(), BoxSelectTool())
# Copy and paste from the imports line.

output_file('file_name_goes_here.html')
show(plot)