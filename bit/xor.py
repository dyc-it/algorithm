#-*- coding:utf-8 –*-

def add_by_xor(x, y):
    print "orgion:x=%s----%d" % (bin(x), x)
    print "orgion:y=%s----%d" % (bin(y), y)
    result = y
    i = 0

    # 不能理解的地方在于,为什么x一定会等于0
    # 解释:假设x为m位,y为n位(且m>=n),则x^y的最大位数不会超过m。
    # 如果循环一直不结束,那么x会不断地左移,直到左移到m的低n位全为0;此时如果进行x&y操作,结果一定为0,x=(x&y)<<1的结果也是0.
    # 此时x=0,循环结束
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


if __name__ == '__main__':
    x, y = 17, 3
    result = add_by_xor(x, y)
    print result
