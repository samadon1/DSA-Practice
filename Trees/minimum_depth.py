"""
Find the minimum depth of a binary binary tree. The minimum depth is number of nodes along the shortest path from 
the root node to the nearest leaf node

Input: Root of a BT
Output: Minumum depth of the binary tree

                             1
                            / \
                           2   3            ---> Minimum depth is 2
                          / \
                         4   5



"""

from collections import deque

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def minimum_depth(root):
    queue = deque()
    minDepth = 1

    if root is None:
        return minDepth

    queue.append(root)

    while queue:
        levelSize = len(queue)

        for _ in range(levelSize):
            current = queue.popleft()

            if current.left is None and current.right is None:
                return minDepth
            else:
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
                minDepth += 1
    
    return minDepth

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(minimum_depth(root))