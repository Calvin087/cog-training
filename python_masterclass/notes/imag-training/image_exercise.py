from PIL import Image

text_image = Image.open('image_link.PNG')
black_image = Image.open('cover_image.PNG')

width = 1226
height = 777

black_image = black_image.resize((width, height))

print(text_image.size)

black_image.putalpha(50)

text_image.paste(black_image, box=None, mask=black_image)
text_image.show()