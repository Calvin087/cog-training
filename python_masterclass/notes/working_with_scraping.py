import requests
from bs4 import BeautifulSoup, SoupStrainer
import os


res1 = requests.get('https://en.wikipedia.org/wiki/Cicada_3301')

soup1 = BeautifulSoup(res1.text, 'html.parser')

cicada_content = soup1.select('.thumbimage') # <-- list with single with img tag

cicada_content_image = "http:" + cicada_content[0]['src']
# we have a list of images == 1,
# grab the first one to get html tags,
# add http string that's missing
# then dictionary call ['src'] to get url

final_image_link = requests.get(cicada_content_image)

file_insert = open('/Users/calvin/Documents/GitHub/cog-training/python_masterclass/bs4_scraps/cicada_img_new.jpg', 'wb')
# This creates a new file for me
# Write and Binary permissions = wb

file_insert.write(final_image_link.content)
file_insert.close()
# before this works i have to GET this item.content <- content is important
# Right now it's a STR which fails