# flake8:NOQA
import urllib2


uri = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='


def get_next(tries, next=12345):
    for _ in xrange(tries):
        u = urllib2.urlopen(uri + str(next))
        raw = u.read()
        print raw
        yield raw
        next = raw.split(' ')[-1]


#print('\n'.join([n for n in get_next(100)]))

# and the next nothing is 16044
# Yes. Divide by two and keep going.

print('\n'.join([n for n in get_next(200, next=16044 / 2)]))

#There maybe misleading numbers in the 
#text. One example is 82683. Look only for the next nothing and the next nothing is 63579
