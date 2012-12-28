# flake8: NOQA
from PIL import Image
from itertools import groupby

image = Image.open('oxygen.png')
img = image.convert("RGBA")

data = img.load()

#print [data[3, ind] for ind in xrange(43,54)]

pixels = [data[ind, 43] for ind in xrange(img.size[0])]
chars = ''.join([chr(data[i*7, 43][0]) for i in xrange(img.size[0]/7)])
print chars

l = [105, 110, 116, 101, 103, 114, 105, 116, 121]
print '[105, 110, 116, 101, 103, 114, 105, 116, 121] is "%s"' % ''.join(map(chr, l))

#grouped = [list(g) for k, g in groupby(pixels)]
#print filter(lambda x: x != '1', map(lambda x: chr(len(x)*7), grouped))

counter = 0
previous_color = pixels[0]
for pixel in pixels:
    if pixel != previous_color:
        #print 'counter is %d' % counter
        counter = 1
    else:
        counter += 1

# color replacement
#for y in xrange(img.size[1]):
    #for x in xrange(img.size[0]):
        #if data[x,y] == (115, 115, 115, 255):
            #data[x,y] = (255, 255, 255, 255)

#img.show()
