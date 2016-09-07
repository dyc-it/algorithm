#!/usr/env python
#i个人最后一个出环的编号=(i-1个人最后一个出环的编号+k)%i

#m表示初始情况下环的总人数，k表示报数的值，i表示m个人中第i个人出环的编号！
def joseph_ring_step(m, k, i):
    if i == 1:
        return (m+k-1) % m
    else:
        return (joseph_ring_step(m-1, k, i-1)+k) % m

if __name__ == '__main__':
    m = 10
    k = 3
    for i in range(1, m+1):
        print 'NO.%d out label:%d' %(i, joseph_ring_step(m, k, i))
