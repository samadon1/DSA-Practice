"""
Given the root of a binary tree, return the level order traversal of its nodes' values (i.e from left
to right, level order by level)

          3           [3]
        /   \
       1      4       [1, 4]
      / \    / \
     6   9  2   3     [6, 9, 2, 3]

     Approach:
     1. If root is not none, add to the first level
     2. For the root's children, add to the second level
     3. For the number of nodes at each level, add their children to the next level

"""

from collections import deque


def traversal(root):
  res = []
  queue = deque()
  visited = set()

  if root is None:
    return res

  queue.append(root)
  while queue:
    levelSize = len(queue)
    currentLevel = []
    for _ in range(levelSize):
      current = queue.popleft()
      visited.add(current)

      currentLevel.append(current)

      if current.left:
        queue.append(current.left)
      if current.right:
        queue.append(current.right)

    res.append(currentLevel)
  
  return res

      



