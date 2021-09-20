import array as arr
import math
from typing import Union, Tuple


def find_max_subarray_brute_force(array: arr.array) -> Tuple[int, int, Union[int, float]]:
    left = None
    right = None
    best_sum = -math.inf

    for i in range(len(array)):
        cumulative_sum = array[i]
        for j in range(i + 1, len(array)):
            cumulative_sum += array[j]

            if cumulative_sum > best_sum:
                left = i
                right = j
                best_sum = cumulative_sum

    return left, right, best_sum


def find_max_crossing_subarray(array: arr.array,
                               low: int,
                               mid: int,
                               high: int) -> Tuple[int, int, Union[int, float]]:
    left_sum = -math.inf
    temp_sum = 0
    max_left = None
    for i in reversed(range(low, mid + 1)):
        temp_sum += array[i]
        if temp_sum > left_sum:
            left_sum = temp_sum
            max_left = i

    right_sum = -math.inf
    temp_sum = 0
    max_right = None
    for j in range(mid + 1, high + 1):
        temp_sum += array[j]
        if temp_sum > right_sum:
            right_sum = temp_sum
            max_right = j

    return max_left, max_right, left_sum + right_sum


def find_max_subarray(array: arr.array,
                      low: int,
                      high: int) -> Tuple[int, int, Union[int, float]]:
    if high == low:
        return low, high, array[low]  # base case

    mid = math.floor((low + high) / 2)
    left_low, left_high, left_sum = find_max_subarray(array=array, low=low, high=mid)
    right_low, right_high, right_sum = find_max_subarray(array=array, low=mid + 1, high=high)
    cross_low, cross_high, cross_sum = find_max_crossing_subarray(array=array, low=low, mid=mid,
                                                                  high=high)

    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_low, left_high, left_sum
    if right_sum >= left_sum and right_sum >= cross_sum:
        return right_low, right_high, right_sum
    return cross_low, cross_high, cross_sum
