"""
You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node.
If such a node does not exist, return null.
"""


from collections import deque

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.right = right
        self.left = left


def node_of_bst(root, val):
    queue = deque()
    res = []
    
    if root is None:
       return None

    queue.append(root)

    while queue:
        
        levelSize = len(queue)
        for _ in range(levelSize):
            current = queue.popleft()
        
            #if node's value equals val
            if current.val == val:
                if current.left:
                    res.append(current.left.val)
                if current.right:
                    res.append(current.right.val)
	    
            #else if current not equal to val
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
    
    return res if res is not None else None


root =  TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)


S = 2

print(node_of_bst(root, S))