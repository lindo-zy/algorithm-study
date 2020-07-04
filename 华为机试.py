#!/usr/bin/python3
# -*- coding:utf-8 -*-


# 集五福算法
s = input()
ls = s.split(',')
ans = [0, 0, 0, 0, 0]
for item in ls:
    for index, x in enumerate(item):
        ans[index] += int(x)

print(min(ans))

# 给定数字求最大时间
import itertools

ans = []
ls = [1, 2, 3, 4, 5, 6]
for item in itertools.permutations(ls):
    if item[:2] > (2, 3) or item[2:4] > (5, 9) or item[4:] > (5, 9):
        continue
    ans.append('%d%d:%d%d:%d%d' % item)
print(max(ans))


# 孤岛问题
def numIsLand(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] > '0':
                count += 1
                dfs(grid, i, j)
    return count


def dfs(grid, i, j):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid):
        return
    grid[i][j] = '0'
    dfs(grid, i, j - 1)
    dfs(grid, i + 1, j)
    dfs(grid, i, j + 1)
    dfs(grid, i - 1, j)
