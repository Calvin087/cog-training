import re
from bokeh.io import output_file, show
from bokeh.models import GMapPlot, GMapOptions, ColumnarDataSource, Circle, Range1d, PanTool, WheelZoomTool, BoxSelectTool
import hashlib
from cryptography.fernet import Fernet
import base64

f = open('message_new_pen.txt')

text = f.read()

# print(text)

pattern1 = r'[\d]+.[\d]+,-[\d]+.[\d]+'

results = re.findall(pattern1, text)
split = results[0].split(',')

lats = []
lons = []

for num in results:
    lat, lon = num.split(',')
    lats.append(float(lat))
    lons.append(float(lon))

map_options = GMapOptions(lat=0, lng=0, zoom=5)

plot = GMapPlot(x_range=Range1d(), y_range=Range1d(), map_options=map_options)

plot.title.text = 'Something interesting here'

plot.api_key = input('Paste API key here: ')

source = ColumnarDataSource(data=dict(lat=lats,long=lons))

circle = Circle(x='lon', y='lat', size=10, fill_color='red')

plot.add_glyph(source, circle)

plot.add_tools(PanTool(), WheelZoomTool(), BoxSelectTool())

output_file('gmap_plot.html')


#-------------------

the_keyword = b'TRUTH'

key = hashlib.sha3_256(the_keyword)

key_bytes = key.digest()

fernet_key = base64.urlsafe_b64encode(key_bytes)

print(fernet_key)

custom_cipher = Fernet(fernet_key)

message = b'gAAAAABaUXStIpjRWJTrbWGOB45IyRpbb8Zyl1sdktcSeOL0zpH-_Oxd2nXVjeph_fGybthCci75lTd0z5SycthFo-5uoFxZqeBTdDc_n9uq3FdZk75gYFAWIRSGlAqlBQlcqkNhVx3W3w7rTaCAhCrHijeyTtxq53S3ab6fLHUw3KPHx2LtdurISe5ArhrmG9IOepnzGzBBTaTgCfoAmbITCWbp_5cdQQ=='

final = custom_cipher.decrypt(message)

print(final)

#-------------------