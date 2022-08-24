"""
Given a binary tree, populate an array to represent the averages of all of its levels

Input: Root of binary tree
Output: Array of level averages

                         1          [1]
                        / \
                       2   3        [2.5]
                      / \
                     4   5          [4.5]

"""
from collections import deque

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def average_of_levels(root):
    queue = deque()
    res = []

    if root is None:
        return res

    queue.append(root)
    while queue:
        sum = 0
        levelSize = len(queue)
        average = 0.0

        for _ in range(levelSize):
            current = queue.popleft()
            sum += current.val

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        average = sum / levelSize

        res.append(average)
    return res

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(average_of_levels(root))

