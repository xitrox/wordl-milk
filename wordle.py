# coding=utf-8

from PIL import Image, ImageDraw, ImageFont
from datetime import date
import sys

left = 0
top = 80
padding = 80

if (len(sys.argv) > 1):
    s = sys.argv[1]
else:
    exit()
lines = s.split("\n")

out = Image.new("RGBA", (400, 600), (255, 255, 255, 255))
fnt = ImageFont.truetype("Roboto-Regular.ttf", 50)
d = ImageDraw.Draw(out)

d.text((0, 0), lines[0], (0, 0, 0), font=fnt)
green = Image.open('./assets/green.png').convert('RGBA')
white = Image.open('./assets/white.png').convert('RGBA')
orange = Image.open('./assets/orange.png').convert('RGBA')
black = Image.open('./assets/black.png').convert('RGBA')

mask_milk = Image.open('./assets/mask_milk.png').convert('RGBA')
milk = Image.open('./assets/milk.jpg').convert('RGBA')
mask_bro = Image.open('./assets/mask_bro.png').convert('RGBA')
bro = Image.open('./assets/bro.jpg').convert('RGBA')


colorBlocks = lines[2:]
for line in colorBlocks:
    for block in line:
        if(block == '🟩'):
            out.paste(green, mask=green, box=(left, top))
        if(block == '⬜'):
            out.paste(white, mask=white, box=(left, top))
        if(block == '🟨'):
            out.paste(orange, mask=orange, box=(left, top))
        if(block == '⬛'):
            out.paste(black, mask=black, box=(left, top))
        left += padding
    left = 0
    top += padding


out = out.resize((160, 240))
bro_out = out.resize((100, 150)).crop((0, 0, 100, 100))

box_milk = (70, 260)
box_bro = (340, 150)

bro.paste(mask_bro, mask_bro)
bro.paste(bro_out, box_bro)
bro.save('wordle_bro_%s.png' % date.today())

milk.paste(mask_milk, mask=mask_milk)
milk.paste(out, box_milk)

milk.save('wordle_%s.png' % date.today())
