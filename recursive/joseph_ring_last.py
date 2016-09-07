#!/usr/env python
#只求出最后一个出环的编好，不要求中间过程
#i个人最后一个出环的编号=(i-1个人最后一个出环的编号+k)%i

#m表示初始情况下环的总人数，k表示报数的值
def joseph_ring_last(m, k):
    last = 0
    for i in range(2, m+1):
        last = (last + k)%i
    return last + 1

if __name__ == '__main__':
    print joseph_ring_last(1, 3)
    print joseph_ring_last(2, 3)
    print joseph_ring_last(3, 3)
    print joseph_ring_last(4, 3)