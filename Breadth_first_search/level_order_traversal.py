"""
Given a binary tree, populate an array to repre its level-by-level traversal. You should populate the values of all nodes of
each level from left to right in separate subarrays.

"""

class Tree:
    def __init__(self, val):
        self.val = val
        self.left  = None
        self.right = None

def levelTraversal(root):
    queue = [root]
    visited = [root]
    res = []

    while queue:
        currentLevel = []
        level_Size = len(queue)
        

        for _ in range(level_Size):
            current = queue.pop(0)
            currentLevel.append(current.val)
            # print(current.val)


            if current.left:
                queue.append(current.left)
                visited.append(current.left)
            if current.right:
                queue.append(current.right)
                visited.append(current.right)
        res.append(currentLevel)
    return res

newTree = Tree(1)
newTree.left = Tree(2)
newTree.right = Tree(3)
newTree.left.left = Tree(4)
newTree.left.right = Tree(5)
newTree.right.right = Tree(7)
newTree.right.left = Tree(6)


print(levelTraversal(newTree))

            



