#!/usr/env python


def hanoi_tower(n, start_tower, middle_tower, end_tower):
    if n == 1:
        print 'from ' + start_tower + ' to ' + end_tower
    else:
        hanoi_tower(n-1, start_tower, end_tower, middle_tower)
        print 'from ' + start_tower + ' to ' + end_tower
        hanoi_tower(n-1, middle_tower, start_tower, end_tower)


if __name__ == '__main__':
    hanoi_tower(3, 'A', 'B', 'C')
