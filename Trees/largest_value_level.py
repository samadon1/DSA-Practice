"""
Given a binary tree, find the largest value on each level.


Input: Root of BT
Output: Array of largest value of each level

                 1          1
                / \
               2   3        3
              / \
             4   5          5
"""

from collections import deque

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def largest_level_value(root):
    queue = deque()
    res =  []

    queue.append(root)
    while queue:
        levelMax = 0
        levelSize = len(queue)
        for _ in range(levelSize):
            current = queue.popleft()
            levelMax = max(levelMax, current.val)

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        res.append(levelMax)
    return res


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(largest_level_value(root))