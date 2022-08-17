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
    array = sorted(array)      
    res = []                         #Sort the array
    for i in range(len(array)):
        if i > 0 and array[i] == array[i-1]:
            continue                         #For each element in the array
        
        l, r = i+1, len(array) - 1                      #create a right pointer and a left pointer for the other pairs
        target = -array[i]                              # target should be the neg of the first element
        while l < r:
            sum = array[l] + array[r]   
            if sum == target:                           #If they are the same
                res.append([array[i], array[r], array[l]])     #return the triples
                l +=1
                r -=1
                while l < r and array[l] == array[l-1]:
                    l += 1
                while l < r and array[r] == array[r+1]:
                    r -= 1
            elif(sum > target):                     
                r -= 1                                  #if the sum is greater than target decrement right pointer 
            else:
                l += 1                                  #if the sum is less than target increment left pointer
    return res

array = [-3, 5, 1,0,-2 , 2]
print(triplet_sum(array))
