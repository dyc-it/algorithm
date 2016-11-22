# -*- coding:utf-8 -*-
import random

"""
Longest increasing subsequence,最长递增子序列问题。
在一个给定的数值序列中，找到一个子序列，使得这个子序列元素的数值依次递增，
并且这个子序列的长度尽可能地大。最长递增子序列中的元素在原序列中不一定是连续的。
"""


def lis_dp(sequence):
    length = len(sequence)
    # 保存以原序列sequence中每个元素结尾的子数列的lis,默认值为1
    sub_sequence_lis = [1] * length

    for i in xrange(0, length):
        max_len = 0

        # 遍历Ai前面的每一个元素Aj
        for j in xrange(0, i):
            # 需要满足Aj<Ai并且LSI最大的子序列。找到LSI最大的子序列之后,加上1就是Ai的LIS了。
            if sequence[i] > sequence[j] and max_len < sub_sequence_lis[j]:
                max_len = sub_sequence_lis[j]
        sub_sequence_lis[i] = max_len + 1

    # sub_sequence_lis的最大值就是原sequence的lsi
    return max(sub_sequence_lis)


def lis_nlogn(sequence):
    lis = 1
    length = len(sequence)
    lis_location = [0] * (length + 1)
    lis_location[1] = sequence[0]

    for i in xrange(1, length):
        # 先找到插入的位置
        position = get_position(lis_location, 1, lis, sequence[i])
        # 在找到的位置插入元素
        lis_location[position] = sequence[i]

        # 如果是在
        if lis < position:
            lis = position
    return lis


# 在lis_location有序序列上,找到第一个大于等于key的位置;如果都小于key,返回end+1
def get_position(lis_location, start, end, key):
    if lis_location[end] <= key:
        return end + 1
    while start < end:
        mid = start + (end - start) / 2
        if lis_location[mid] <= key:
            start = mid + 1
        else:
            end = mid
    return start


if __name__ == "__main__":
    sequences = [[5, 6, 7, 1, 2, 8],
                 [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15],
                 random.sample(range(0, 10000), 2000)]

    for sequence in sequences:
        LIS = lis_dp(sequence)
        print "lis_dp of the array is: %d" % LIS
        LIS = lis_nlogn(sequence)
        print "lis_nlogn of the array is: %d" % LIS
