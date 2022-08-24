"""
Given a binary tree and a node, find the level order successor of the given node in the tree. The level order
order successor is the node that appears right after the given node in the level order traversal

Input: Root of BT and node
Output: Successor of node

                    Node is 3
                    Successor of 3 is 4

                         1
                        / \
                       2   3
                      / \
                     4   5

"""

from collections import deque

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.right = right
        self.left = left

def successor_node(root, node):
    queue = deque()
    suc = TreeNode(None)

    if root is None:
        return suc
    
    queue.append(root)
    while queue:
        levelSize = len(queue)

        for _ in range(levelSize):
            current = queue.popleft()

            if current.left:
                    queue.append(current.left)
            if current.right:
                    queue.append(current.right)

            if current.val == node.val:
                suc = queue.popleft()

    return suc.val


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

node = TreeNode(3)

print(successor_node(root, node))


