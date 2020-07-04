# -*- coding:utf-8 -*-

import time
import sys

sys.setrecursionlimit(9000000)


# 直接递归
def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)


# 带备忘录递归
def fib2(n):
    if n < 1:
        return 0
    memo = [0] * (n + 1)
    return helper(memo, n)


def helper(memo, n):
    if n == 1 or n == 2:
        return 1
    if memo[n] != 0:
        return memo[n]
    memo[n] = helper(memo, n - 1) + helper(memo, n - 2)

    return memo[n]


# dp迭代
def fib3(n):
    dp = [0] * (n + 1)
    dp[1] = dp[2] = 1
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


# dp优化
def fib4(n):
    if n == 1 or n == 2:
        return 1
    prev = 1
    curr = 1
    for i in range(3, n + 1):
        s = prev + curr
        prev = curr
        curr = s
    return curr


if __name__ == '__main__':
    start = time.time()
    print(start)
    # print(fib(200))
    # print(fib2(2000))
    # print(fib3(20000)) #0.0312497615814209
    # print(fib4(20000)) #0.015624761581420898

    print(time.time() - start)
