# flake8: NOQA
import pickle
import urllib2
import sys

#u = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/banner.p')
#banner = ''.join(map(lambda x: x.strip(), u.readlines()))
#print banner

with open('banner.p', 'r') as fd:
    mapped = pickle.load(fd)

def print_string(string):
    for (count, char) in string:
        print char*count,
    print '\n',

def compose_column(string):
    s = ''
    for (count, char) in string:
        s += char*count
    return reversed(s)

map(print_string, mapped)
print
map(lambda x: sys.stdout.write(''.join(x)+'\n'), zip(*map(compose_column, mapped)))


