from itertools import groupby

def morris(start='1', now=0, times=30):
    if now == times:
        return start
    acc = ''
    for k, g in groupby(start):
        acc = acc + str(len(list(g))) +  str(k)
    return morris(acc, now + 1, times)

print len(morris())
