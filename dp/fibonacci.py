# -*- coding:utf-8 -*-
"""
fibonacci数列的普通解法和动态规划解法。
"""


def fibonacci_normal(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci_normal(n - 1) + fibonacci_normal(n - 2)


tmp_result = dict()
tmp_result[0] = 0
tmp_result[1] = 1


def fibonacci_dp(n):
    if n not in tmp_result:
        tmp_result[n] = fibonacci_dp(n - 1) + fibonacci_dp(n - 2)
    return tmp_result[n]


if __name__ == '__main__':
    n = 30
    normal = fibonacci_normal(n)
    print "normal result is %d" % normal

    dp = fibonacci_dp(n)
    print "dp result is %d" % dp
