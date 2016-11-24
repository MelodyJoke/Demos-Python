#! /usr/bin/python

import math

# test in first installation
print('Hello Venus!')


def euclid(left, right):
    """
        欧几里得算法
        两个非负整数的最大公约数问题
        1.若其中一个数为0， 则另一个数为问题的解
        2.较大数除以较小数的余数， 与较小数的最大公约数为问题的解
    """
    if left >= right:
        temp = left
        left = right
        right = temp
    if left == 0:
        return right
    return int(euclid(math.fmod(right, left), left))


# 欧几里得最大公约数算法
inpLeft = int(input('type in two positive integers:\n'))
inpRight = int(input(''))
print('the greatest divisor of', inpLeft, 'and', inpRight, 'is', '%d.' % euclid(inpLeft, inpRight))
print('hello')