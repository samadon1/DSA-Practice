"""
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

Given two arrays preorder and inorder contruct the original binary tree.
Input: Two arrays
Output: root

preorder: root -> left -> right
inorder: left -> root -> right


preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]

				 3
				/ \
			  9    20
             / \
           15   7

1. Determine root node from preorder - first element of the preorder array
2. Determine the left nodes of the tree from the inorder - elements of the left of root node in inorder
3. Determine the right nodes from the right of the root value on inorder array
4. Arrange right nodes to the root:
      I. First value is the root/child node, next element is the left and the subsequent value is the right

"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def contruct_binary_tree(preorder, inorder):
    root = preorder[0]
    root_position = inorder.index(root)
    left_children = inorder[:root_position]
    right_children = inorder[root_position + 1 :]

    root = TreeNode(root)
    root.left = populate_children(left_children)
    root.right = populate_children(right_children)
    
    def populate_children(nodes):
	    
        for end in range(nodes):
            start = 0
            window = end - start
            
            if  window == 2:
                node = TreeNode(nodes[0])
                node.left = TreeNode(nodes[1])
                node.right = TreeNode(nodes[2])
                start += 3
                root = nodes[end + 1]
			
            elif nodes and window == 1:
                node = TreeNode(nodes[0])
                node.left = TreeNode(nodes[1])
            else:
                node = TreeNode(None)
        return nodes[0] if not None else None	
	



				
