"""
Given the root of a binary tree, return the reverse level order of its nodes' values

              1                 [1]
             / \
            2   3               [2,3]
           / \
          4   5                 [4,5]

Input: Root of BT
Output: [[4,5], [2,3], [1]]

"""

from collections import deque

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def reverse_level_order(root):
    queue = deque()
    res = deque()

    if root is None:
        return 0

    queue.append(root)
    while queue:
        currentLevel  = []
        levelSize  = len(queue)

        for _ in range(levelSize):
            current = queue.popleft()
            currentLevel.append(current.val)

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        res.appendleft(currentLevel)
    return res


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.right = TreeNode(5)

print(reverse_level_order(root))
    