"""
Given an array, find the average of all contigous subarrays of size k in it

Example:
Input: [1,3,2,6,-1,4,1,8,8,2], k =3

Approah: 
1. for every element in the array except the overlaping elements,
2. For every element , we find a window
3. Calculate the average of the window 
4. Add avergae to the average_list

"""


from array import array


def average_subarray(array, k):

    average_list = []
    for i in range(len(array)-k+1):  #account for overlapping elements
        sum = 0
        for j in range(i, i + k):    #create the window
            sum += array[j]
        average_list.append(sum/k)
    return average_list




def average_subarray1(array, k):
    average_list = []
    start, sum = 0, 0.0

    for end in range(len(array)):
        sum += array[end]

        while end >= k -1:
            average_list.append(sum/k)
            sum -= array[start]
            start += 1

    return average_list

array = [1,3,2,6,-1,4,1,8,8,2]
print(average_subarray1(array, 3))

