class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left =None
        self.right =None

def dfs(root):
    stack = []
    stack.append((root, ""))

    def isLeaf(current):
        return current.left is None and current.right is None

    while stack:
        current, path = stack.pop()
        delim = " -> " if path else "\n"
        nodeToPath = str(current.val) + delim + path

        if isLeaf(current):
             print(nodeToPath)

        if current.left:
            stack.append((current.left, nodeToPath))
        if current.right:
            stack.append((current.right, nodeToPath))

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print(dfs(root))

"""
                       1 
                    /    \
                   2      3
                  / \    / \
                 4   5  6   7


                 """