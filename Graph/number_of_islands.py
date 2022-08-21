"""
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

"""

import collections

def number_of_islands(grid):
    q = collections.deque()
    visited = set()
    islands = 0
    rows = len(grid)
    cols = len(grid[0])

    def bfs(r,c):
        q.append((r,c))
        visited.add((r,c))

        while q:
            r, c = q.popleft()
            directions = [[1,0], [-1,0], [0,1], [0,-1]]

            for dr,dc in directions:
                r,c  = dr + r, dc + c
                if r in range(rows) and c in range(cols) and (r,c) not in visited and grid[r][c] == 1:
                        q.append((r,c))
                        visited.add((r,c))


    if not grid:
        return 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (r,c) not in visited:
                bfs(r,c)
                islands += 1
    return islands

    
grid = [
        [1,1,1,0,0],
        [1,1,0,1,1],
        [1,1,0,0,0],
        [0,0,0,1,1]
]

print(number_of_islands(grid))
            
