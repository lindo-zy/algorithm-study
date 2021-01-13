#!/usr/bin/python3
# -*- coding:utf-8 -*-


def binarySearch(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = left + (right - left) / 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
    return -1
