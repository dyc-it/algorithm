#!/usr/env python

def arrangement(str, k, m):
    if k==m:
        print str
    else:
        for i in range(k, m+1):
            str[k], str[i] = str[i], str[k]
            arrangement(str, k+1, m)
            str[k], str[i] = str[i], str[k]


if __name__ == '__main__':
    str = 'abc'
    print 'the arrangement of %s follows:' % str
    arrangement(list(str), 0, len(str)-1)

