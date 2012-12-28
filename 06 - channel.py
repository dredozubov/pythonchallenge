# flake8: NOQA
import zipfile
import sys

def zipme(zf, filename='90052'):
    while True:
        try:
            string = zf.open(filename+'.txt', 'r').read()
        except KeyError:
            break
        #print string
        print zf.getinfo(filename+'.txt').comment
        filename = string.split(' ')[-1]


with zipfile.ZipFile('channel.zip', 'r') as zf:
    print zf.open('readme.txt', 'r').read()
    zipme(zf)
    print
    #print ''.join([info.comment for info in zf.infolist()])
