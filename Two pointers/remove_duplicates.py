"""
Given an array of sorted numbers, remove all duplicates from it. You should not use extra space. After removing 
duplicates in-place, return the new length of the array

Input: Sorted array
Output: Interger

Example: 
Input: [0,0,1,1,1,2,2,3,3,4]
Output: 5

Approach: 
1. Iterate over the array 
2. If element exists, move to next element
3. If element is new  add to seen
4. return the length of seen

"""
#my answer using extra space
def remove_duplicates(array):
    hashset = set()
    for i in range(len(array)):
        if array[i] not in hashset:
            hashset.add(array[i])
    
    return len(hashset)

#using two pointers
def remove_duplicates1(array):
    l = 1   #Start at index 1 since index 0 is unique
    for r in range(1, len(array)): # Start right pointer also at index 1
        if array[r] != array[r]:   # If right element not the same as its previous element: 
            array[l] = array[r]    # Left pointer is replaced by element at the right 
            l +=1                  # Increment left pointer by 1
    return l                       # return l at the end of the program

array = [0,0,1,1,1,2,2,3,3,4]
print(remove_duplicates(array))