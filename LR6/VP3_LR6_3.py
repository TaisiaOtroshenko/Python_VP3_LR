from PIL import Image, ImageDraw

im = Image.new('RGB', (400, 300), (100, 193, 200))
draw = ImageDraw.Draw(im)

draw.rectangle((0,250,400,300), fill='green')

draw.line((150, 50, 200, 100), fill='brown', width=5)
draw.line((250, 50, 200, 100), fill='brown', width=5)

draw.polygon((200,125, 300,50, 300,230, 200,175, 100,230, 100,50, 200,125), (120, 30, 70))
draw.ellipse((185, 100, 215, 200), fill='pink', outline=(255,255,255))

draw.ellipse((120,120,150,150), fill='yellow')
draw.ellipse((250,120,280,150), fill='yellow')

draw.ellipse((150,170,160,180), fill='yellow')
draw.ellipse((240,170,250,180), fill='yellow')

im.show()
im.save('butterfly.jpg')