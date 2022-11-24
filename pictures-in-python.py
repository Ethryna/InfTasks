from PIL import Image, ImageDraw, ImageFont
"""im1 = Image.open('C:/Users/user/Documents/142 б/pictures/1.jpg')
im2 = Image.open('C:/Users/user/Documents/142 б/pictures/2.jpg')
im3 = Image.open('C:/Users/user/Documents/142 б/pictures/3.jpg')
im1.show()
im2.show()
im3.show()"""

def ImText(s):
    im = Image.new('RGB', (800, 600), color = ('#007E66'))
    font1 = ImageFont.truetype('C:/Windows/Fonts/MISTRAL.TTF', size=36)
    draw = ImageDraw.Draw(im)
    draw.text((140,70), s, font=font1, fill=('#0A0000'))
    im.show()

ls = []
for i in range(10):
    ls.append(input(f'Введите текст {i+1}: '))
for j in range(10):
    ImText(ls[j])
