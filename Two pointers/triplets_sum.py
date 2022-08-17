"""
Given an array of unsorted numbers, find all unique triplets in it that add up to zero

Input: unsorted array
Output: an array triplet

Example:
Input: [-3, 4,2, 4, 1]
Output: [-3,2,1]

Approach: 
1. Iterate over every element
2. For every element, find the other unique pairs that add up to the opposite of the element

"""

def triplet_sum(array):
    array = sorted(array)                               #Sort the array
    for i in range(len(array)):                         #For each element in the array
        
        l, r = i+1, len(array) - 1                      #create a right pointer and a left pointer for the other pairs
        target = -array[i]                              # target should be the neg of the first element
        while l < r:
            sum = array[l] + array[r]   
            if sum == target:                           #If they are the same
                return array[i], array[r], array[l]     #return the triples
            elif(sum > target):                     
                r -= 1                                  #if the sum is greater than target decrement right pointer 
            else:
                l += 1                                  #if the sum is less than target increment left pointer
    return 0

array = [-3, 5, 1,0,-2 , 2]
print(triplet_sum(array))
