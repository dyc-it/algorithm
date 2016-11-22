# -*- coding:utf-8 -*-
# !/usr/evn python


def lastBallLocation(depth, count):
    # initialize all switchs with closed status
    switchs = [False] * (1 << depth)
    n = (1 << depth) - 1  # n indicates the maximum label of the ball
    k = n

    for i in range(0, count):  # traverse route of all the balls
        k = 1  # the ball start from root node with label 1
        while True:
            switchs[k] = not switchs[k]  # when the ball comes, the switch reverser its status
            if switchs[k]:  # if switch is open, go left
                k = 2 * k
            else:  # if switch is closed, go right
                k = 2 * k + 1
            if k > n:  # when k is bigger than n, the ball arrives the bottom
                break
    # when all balls arrive the bottom, the k value divided by 2 is the label of the last ball's terminal point
    print k / 2


def dropping_balls(depth, ball_count):
    # 树从1开始编号, 那么除了叶子节点外,每个编号为k的结点的左孩子编号为2k,右孩子编号为2k+1。
    max_tree_node = (1 << depth) - 1  # 注意:在python中移位运算的优先级小于加法和减法运算
    # 开关是一个list,从0开始编号;但是我们希望开关编号和树的编号对应起来。所以开关列表的长度比树的结点总数多1个,编号为0的开关不使用
    switches = [False] * (max_tree_node + 1)
    for i in xrange(0, ball_count):
        k = 1
        while True:
            switches[k] = not switches[k]
            # k = 2 * k if switches[k] else (2 * k + 1)
            if switches[k]:  # if switch is open, go left
                k = 2 * k
            else:  # if switch is closed, go right
                k = 2 * k + 1
            if k > max_tree_node:
                break
    return k / 2


if __name__ == '__main__':
    depths = [1, 2, 3, 5, 2, 16]
    counts = [1, 1, 1, 1, 2, 12345]
    for i in range(0, len(depths)):
        lastBallLocation(depths[i], counts[i])

    input = [(1, 1), (2, 1), (3, 1), (5, 1), (2, 2), (16, 12345)]
    for pair in input:
        depth = pair[0]
        ball_count = pair[1]
        drop_out_location = dropping_balls(depth, ball_count)
        print "the last location of ball is: %d" % drop_out_location
