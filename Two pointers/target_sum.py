"""
Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given number
target

Input: Sorted array and integer
Output: An array pair

Example:
Input: 6, [1,2,3,4,5,6]
Output: [4,2]

Approach:

1. Iterate over each element
2. For each element compare it to the remaining elements
3. If they sum to the target, return both elements
4. If no such pair exists, return 0

"""
#brute force approach
def target_sum(array, target):
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i] + array[j] == target:
                return array[i], array[j]
    return 0 


#using hashmap
def target_sum1(array, target):
    hashmap = {}
    for i in range(len(array)):
        second = target - array[i]
        if second not in hashmap:
            hashmap[array[i]] = i
        else:
            return array[i], second




#Using two pointers
def target_sum2(array, target):
    l,r = 0, len(array) - 1             #Initialize two pointer at the beginning and the end
    

    while l <   r:                      # While left pointer is less than right pointer
        sum = array[l] + array[r]       #find the sum of the two pointers
        if sum == target:               # if their sum is equal to target
            return array[l], array[r]   #return the element at  both pointers
        elif(target > sum):             #if target is greater, increase left
            l += 1
        else:                           #if target is less, decrease right
            r -= 1 

array = [1,2,3,4,5,6]
target = 6
print(target_sum2(array, target))
