# flake8: noqa
from PIL import Image, ImageDraw

odd = lambda x: bool(x % 2)
even = lambda x: not odd(x)

im = Image.open('cave.jpg')
draw = ImageDraw.Draw(im)

GREY = (256, 256, 256)

for x in xrange(im.size[0]):
        for y in xrange(im.size[1]):
            if odd(x) or even(y):
                draw.point((x,y), GREY)

im.show()
