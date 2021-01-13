#!/usr/bin/python3
# -*- coding:utf-8 -*-
from typing import List


class Node(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: Node, sum: int) -> List[List[int]]:
        if not root:
            return []

        result = []

        def trace_node(pre_list, left_sum, node):
            new_list = pre_list.copy()
            new_list.append(node.val)
            if not node.left and not node.right:
                # 这个判断可以和上面的合并，但分开写会快几毫秒，可以省去一些不必要的判断
                if left_sum == node.val:
                    result.append(new_list)
            else:
                if node.left:
                    trace_node(new_list, left_sum - node.val, node.left)
                if node.right:
                    trace_node(new_list, left_sum - node.val, node.right)

        trace_node([], sum, root)
        return result


if __name__ == '__main__':
    lst = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
    s = 22
    # lst = [10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]
    # s = 8

    sn = Solution()

    print(sn.pathSum(root, s))
