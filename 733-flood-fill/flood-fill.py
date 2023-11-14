#similar to number of islands, except that we call bfs/dfs only once
#flood fill using DFS 
from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.startcolor=image[sr][sc]
        self.cols=len(image[0])
        self.rows=len(image)
        self.visited = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
    
        def dfs(start_row,start_col,grid,color):
            #base conditions
            if (start_row not in range(self.rows)
                or  start_col not in range (self.cols) 
                or grid[start_row][start_col] != self.startcolor 
                or self.visited[start_row][start_col] != 0):
                    return
                    
            self.visited[start_row][start_col]=1
            grid[start_row][start_col]=color
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                dfs(start_row + dr, start_col + dc,grid,color)

        dfs(sr,sc,image,color)
        return image

    # def bfs(self, start_row, start_col,grid,color):
    #     self.visited[start_row][start_col] = 1
    #     grid[start_row][start_col]=color
    #     queue = deque([(start_row, start_col)])
    #     #we will iterate in 4 directions
    #     neighbours=[(-1,0),(0,1),(1,0),(0,-1)]
    #     while queue:
    #         row, col = queue.popleft()
    #         for neighbour in neighbours:
    #                 delta_row = row + neighbour[0]
    #                 delta_col = col + neighbour[1]
    #                 if 0 <= delta_row < self.rows and 0 <= delta_col < self.cols:
    #                     if grid[delta_row][delta_col] == self.startcolor and self.visited[delta_row][delta_col] == 0:
    #                         queue.append((delta_row, delta_col))
    #                         self.visited[delta_row][delta_col] = 1
    #                         grid[delta_row][delta_col]=color



    