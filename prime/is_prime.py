#!/usr/env python
import math


def is_prime(number):
    boundary = int(math.floor(math.sqrt(number)))
    for i in range(2, boundary):
        if number % i == 0:
            return False
    return True


if __name__ == "__main__":
    for j in range(1, 100):
        if is_prime(j):
            print "%d is prime number" % j
















