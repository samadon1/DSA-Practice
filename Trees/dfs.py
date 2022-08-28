from collections import deque
 
 
# A class to store a binary tree node
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
 
 
# Function to check if a given node is a leaf node or not
def isLeaf(node):
    return node.left is None and node.right is None
 
 
def printLeafToRootPaths(root):
 
    # base case
    if not root:
        return
 
    # create an empty stack to store a pair of tree nodes and
    # its path from the root node
    stack = deque()
 
    # push the root node
    stack.append((root, ''))
 
    # loop till stack is empty
    while stack:
 
        # pop a node from the stack and push the data into the output stack
        curr, path = stack.pop()
        print(path)
 
        # add the current node to the existing path
        delim = ' —> ' if path else '\n'
        rootToNodePath = str(curr.data) + delim + path
 
        # print the path if a leaf node is reached
        if isLeaf(curr):
            print(rootToNodePath, end='')
 
        # push the left and right child of the popped node into the stack.
        if curr.right:
            stack.append((curr.right, rootToNodePath))
 
        if curr.left:
            stack.append((curr.left, rootToNodePath))
 
 
if __name__ == '__main__':
 
    ''' Construct the following tree
                1
              /   \
             /     \
            /       \
           2         3
          / \       / \
         /   \     /   \
        4     5   6     7
                 / \
                /   \
               8     9
    '''
 
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.left.left = Node(8)
    root.right.left.right = Node(9)
 
    printLeafToRootPaths(root)
 
