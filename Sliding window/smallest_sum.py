"""
Given an array of positive numbers and a positive number S, find the length of the smallest contiguous subarray whose
sum is greater than or equal to S. Return 0 if no subarray exists

Example:
Input: [2,1,5,2,3,2], S = 7
Output: 2

"""

from array import array
import math
def smallest_sum(array, S):
    start, sum = 0, 0
    min_length = math.inf

    for end in range(len(array)):
        sum += array[end]

        while sum >= S:
            min_length = min(min_length, end - start + 1)
            sum -= array[start]
            start += 1
    if min_length == math.inf:
        return 0
    return min_length 


array = [2, 1, 5, 2, 3, 2]
print(smallest_sum(array, 7))


