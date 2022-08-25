"""
Given a binary tree and a number 'S', find if the tree has a path from root to leaf such that the sum of all the
node values of that equals 'S'.

Input: binary tree and S
Output: True/ False based on whether sum of root to some leaf adds to S
S = 8
                                 1
                                / \
                               2   3
                              / \
                             4   5
"""

class TreeNode:
    def __init__(self, val, left =None , right =None):
        self.val = val
        self.left = left
        self.right = right

def path_from_root(root, S):
    if root is None:
        return False

    if root.val == S and root.left == None and root.right == None:
        return True

    return path_from_root(root.left, S - root.val) or path_from_root(root.right, S - root.val)
    
root  = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

S = 8

print(path_from_root(root, S))