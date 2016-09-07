#!/usr/env python


def joseph_ring(m, k, i):
    print m,
    if i == 1:
        return (m+k-1) % m
    else:
        return (joseph_ring(m-1, k, i-1)+k) % m

if __name__ == '__main__':
    m = 10
    k = 3
    for i in range(1, m+1):
        print 'NO.%d out label:%d' % (i, joseph_ring(m, k, i))
