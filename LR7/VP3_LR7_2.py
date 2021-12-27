# Задача 2. Дано изображение BED.JPG. С помощью инструментов Pillow, 
# добавьте эффект негатива и сделайте надпись GOODNIGHT, 
# сохраните на диск под новым именем BED_1.JPG

from PIL import Image, ImageDraw, ImageFont

image = Image.open("BED.jpg") 
draw = ImageDraw.Draw(image)
pix = image.load()
for i in range(image.size[0]):
    for j in range(image.size[1]):
        p = pix[i, j]
        draw.point((i, j), (255 - p[0], 255 - p[1], 255 - p[2]))

draw.text((100, 250), "GOODNIGHT", ImageFont.truetype("impact.ttf", 40))

image.save("BED_1.jpg")
