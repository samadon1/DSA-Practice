"""
Given an array of positive numbers and a positive number k, find the maximum sum of any contiguous subarray of
size k.

Example:
Input: [2,1,5,1,3,2], k =3

Approach

1. Create two pointer at the start of the array
2. Iterate over every element 
3. if the end pointer is not greater than or equal to k add it to sum
4. Else, if it is greater find the average, substract the start element and increment the start pointer

"""

def max_sum(array, k):
    start, sum = 0, 0
    max_list = []

    for end in range(len(array)):       # add next element to the array
        sum += array[end]

        if end >= k-1:                  #if the index is greater than or equal to k-1
            max_list.append(sum)        #add the sum to the max_list
            sum -= array[start]         # - the first element
            start += 1                  # increment the start pointer
    return max(max_list)

array = [2,1,5,1,3,2]
k = 3
print(max_sum(array,k))