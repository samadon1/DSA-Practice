"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

Root BT; if its a valid BST.
BST: Left node values are less than the node's value and right node values are greater than the node's value

Constraints: Root can be none
Input: Root node
Output: Bool(True/False)

                                              5
                                            /   \
                                           3     9
                                          / \    / \
                                         1   4  8   12
                                                   / \
                                                  10  18
Input: 5
Output: True

1. If root is not None:
    i. Check if the left node value is less than the node's value and the right is greater than the node's value



"""



class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def valid_bst(root):
    # if root is None:
    #     return False

    if not root:
        return True

    if root.left and root.right:
        if not (root.left.val < root.val and root.right.val > root.val):
            return False
    
    return valid_bst(root.left) and valid_bst(root.right)


root = TreeNode(5)
root.left =TreeNode(3)
root.right = TreeNode(9)
root.left.left = TreeNode(1)
root.left.right = TreeNode(4)
root.right.left = TreeNode(8)
root.right.right = TreeNode(12)
root.right.right.left = TreeNode(10)
root.right.right.right = TreeNode(18)

print(valid_bst(root))

