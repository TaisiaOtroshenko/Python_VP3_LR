from PIL import Image, ImageDraw

im = Image.new('RGB', (500, 500), 'white')
draw = ImageDraw.Draw(im)

for i in range(4):
    draw.text((100+i*100,30),text=chr(65+i), fill='brown')
    draw.text((30,100+i*100),text=chr(49+i), fill='brown')
    
    for j in range(4):
        color = (150+(i+j)%2*100,120+(i+j)%2*100,100+(i+j)%2*100)   
        draw.rectangle((50+i*100,50+j*100, 50+(i+1)*100,50+(j+1)*100), color)
im.show()
im.save("chess.jpg")