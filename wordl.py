
from PIL import Image, ImageDraw, ImageFont
import sys

left = 0
top = 80
padding = 80

print(sys.argv[1])
if (sys.argv[1]):
    s = sys.argv[1]

# s = """Wordle 214 2/6

# 🟩⬜⬜🟨⬜
# 🟩🟩🟩🟩🟩
# 🟩🟩🟩🟩🟩
# 🟩🟩🟩🟩🟩
# 🟩🟩🟩🟩🟩
# 🟩🟩🟩🟩🟩"""

"""Wordle 216 4/6

⬜🟩🟩⬜⬜
🟩🟩🟩⬜⬜
🟨⬜⬜🟨⬜
🟩🟩🟩🟩🟩"""

lines = s.split("\n")

out = Image.new("RGBA", (400, 600), (255, 255, 255, 255))
fnt = ImageFont.truetype("Roboto-Regular.ttf", 50)
d = ImageDraw.Draw(out)

d.text((0, 0), lines[0], (0, 0, 0), font=fnt)
green = Image.open('./assets/green.png').convert('RGBA')
white = Image.open('./assets/white.png').convert('RGBA')
orange = Image.open('./assets/orange.png').convert('RGBA')
black = Image.open('./assets/black.png').convert('RGBA')
mask = Image.open('./assets/mask.png').convert('RGBA')


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

milk = Image.open('./assets/milk.jpg').convert('RGBA')

out = out.resize((160, 240))

milk.paste(mask, mask=mask)
milk.paste(out, box=(70, 260))

milk.save('wordle.png')
