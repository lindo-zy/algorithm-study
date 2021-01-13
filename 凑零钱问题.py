#!/usr/bin/python3
# -*- coding:utf-8 -*-

import time


# 暴力递归
def coinChange(coins, amount):
    def dp(n):
        # base case
        if n == 0:
            return 0
        if n < 0:
            return -1
        res = float('INF')
        for coin in coins:
            subproblem = dp(n - coin)
            # 子问题无解
            if subproblem == -1:
                continue
            res = min(res, 1 + subproblem)

        return res if res != float('INF') else -1

    return dp(amount)


# 带备忘录递归
def coinChange2(coins, amount):
    memo = {}

    def dp(n):
        if n in memo:
            return memo[n]
        if n == 0:
            return 0
        if n < 0:
            return -1
        res = float('INF')
        for coin in coins:
            subproblem = dp(n - coin)
            if subproblem == -1:
                continue
            res = min(res, 1 + subproblem)
        memo[n] = res if res != float('INF') else -1
        return memo[n]

    return dp(amount)


# dp迭代法
def coinChange3(coins, amount):
    # 初始化dp
    dp = [amount + 1] * (amount + 1)
    # base case
    dp[0] = 0
    for i in range(len(dp)):
        for coin in coins:
            # 子问题无解
            if i - coin < 0:
                continue
            dp[i] = min(dp[i], dp[i - coin] + 1)
    if dp[amount] == (amount + 1):
        return -1
    else:
        return dp[amount]


if __name__ == '__main__':
    start_time = time.time()
    coins = [1, 2, 3]
    amount = 50
    # print(coinChange(coins, amount))  # 超时
    print(coinChange2(coins, amount))  #
    # print(coinChange3(coins, amount))  # 0.17292189598083496
    print("运行耗时:", time.time() - start_time)
