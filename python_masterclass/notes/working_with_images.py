from PIL import Image

mac = Image.open('image_link1.PNG')

# mac.show()
# Opens image when run

print(mac.size)
print(mac.filename)

# ------- Cropping Images

    # >> (1226, 777) image size

    # x = 0
    # y = 0

    # w = 1226 / 3
    # h = 777 / 10

    # mac.crop((x,y,w,h))

# tutorial doesn't work

# ------- Copying and Pasting
mac.paste(im=location, box=(0,0)) # prob doesn't work

# ------- Resize
mac.resize((3000, 500))

# ------- Rotation
mac.rotate(90)

# ------- Transparency RGBA 0-255
mac.putalpha(0) # Transparent
mac.putalpha(255) # 100% Opaque
mac.putalpha(128) # 50% Opaque

mac.paste(im=otherimage,box=(0,0), mask=otherimage)