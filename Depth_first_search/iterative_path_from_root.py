"""
Given a binary tree and a number 'S', find if the tree has a path from rott to leaf such that the sum of all the
node values of that path equals 'S'

Input: Binary tree and number S
Output: True/ false based on whether the sum of path exists or not

S = 8

                                         1             
                                        / \
                                       2   3
                                      / \
                                     4   5
"""

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.right = right
        self.left = left

def path_from_root(root, S):
    stack = []
    if root is None:
        return False

    stack.append(root)
    while stack:
        levelSize = len(stack)
        for _ in range(levelSize):
            current = stack.pop()

            if current.val == S and current.left is None and current.right is None:
                return True
          
                
            
            
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)
            S -= current.val 
            stack.pop()



root =  TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)


S = 8

print(path_from_root(root, S))
    

    