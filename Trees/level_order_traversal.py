"""
Given the root of a binary tree, return the level order traversal of its nodes' values (i.e from left
to right, level order by level)

Input: Node of a BT
Output: [[1], [2,3], [2,3,4]]

                   1          [1]
                  / \
                 2   3        [2,3]
                / \
               4   5          [4, 5]

1. If root is not Null:
2. Add root to the 1st level
3. Using BFS; for every child of the root node we add them to the next level
4. For every child of every node we add them the the next level
"""
from collections import deque

class TreeNode:
  def __init__(self, val, left = None, right = None):
    self.val = val
    self.left = left
    self.right = right

def level_order_traversal(root):
  queue = deque()
  res = deque()
  
  if root is None:
    return res

  
  queue.append(root)
  
  while queue:
    currentLevel = []
    levelSize = len(queue)

    for _ in range(levelSize):
      current = queue.popleft()
      currentLevel.append(current.val)

      if current.left:
        queue.append(current.left)
      if current.right:
        queue.append(current.right)

      
    res.append(currentLevel) #for reverse, use res.appendleft
  return res


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(level_order_traversal(root))

    
    


  

  