# -*- coding:utf-8 –*-


def add_by_xor(x, y):
    """
    不使用加法, 计算两个数的和。非递归版本
    主要思路:   x + y = x ^ y + (x & y) << 1
    :param x: 被加数
    :param y: 加数
    :return: 两个数的和
    """
    print "orgion:x=%s----%d" % (bin(x), x)
    print "orgion:y=%s----%d" % (bin(y), y)
    result = y
    i = 0

    # 在(x&y)<<1的结果中,如果某位为1,表示该位一定发生了进位。
    # 假设x的位数为m,y的位数为n,那么x+y的位数不会超过num=max(m,n)+1
    # 在第一次循环中,如果某一位发生进位,那么在下一次循环中,该位一定不会发生进位。
    # 因为在本次循环中,如果发生进位,该位结果为0;在下一次循环中,进行&操作,肯定是不会进位了。
    # 进位次数不会超过num次,所以最多循环num次,进位就是0了,循环终止
    while (x != 0):
        i += 1
        print "loop %d" % i

        result = x ^ y
        # result是丢失进位后的和
        print "\tresult is: %s----%d" % (bin(result), result)

        x = (x & y) << 1
        # 此时的x是进位后左移一位保留的进位。为什么要左移一位呢?因为x&y后,如果某一位为1,表示该位应该是进位的,并且进到上一位,所以左移一位。
        # 这么理解 x^y + (x&y)<<1 = x + y
        # 也就是说两个数进行异或操作加上两个数进行与操作后的左移的和,和两个数的和是一样的
        print "\tx is: %s----%d" % (bin(x), x)

        y = result
        print "\ty is: %s----%d" % (bin(y), y)
    return result


def add_by_xor_recur(x, y):
    """
    不使用加法, 计算两个数的和。通过xor实现加法的递归版本
    :param x: 被加数
    :param y: 加数
    :return: 两个数的和
    """
    if x == 0:
        return y
    else:
        sum = x ^ y
        carry = (x & y) << 1
        return add_by_xor(carry, sum)


if __name__ == '__main__':
    x, y = 8, 8
    result1 = add_by_xor(x, y)
    result2 = add_by_xor_recur(x, y)
    print "result1=%d, result2=%d" % (result1, result2)


