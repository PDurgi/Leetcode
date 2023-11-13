from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_count = 0
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.visited = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                if grid[i][j] == "1" and self.visited[i][j] == 0:
                    island_count += 1
                    self.bfs(i, j,grid)
        return island_count

    def bfs(self, start_row, start_col,grid):
        self.visited[start_row][start_col] = 1
        queue = deque([(start_row, start_col)])
        #we will iterate in 4 directions
        neighbours=[(-1,0),(0,1),(1,0),(0,-1)]
        while queue:
            row, col = queue.popleft()
            for neighbour in neighbours:
                    delta_row = row + neighbour[0]
                    delta_col = col + neighbour[1]
                    if 0 <= delta_row < self.rows and 0 <= delta_col < self.cols:
                        if grid[delta_row][delta_col] == "1" and self.visited[delta_row][delta_col] == 0:
                            queue.append((delta_row, delta_col))
                            self.visited[delta_row][delta_col] = 1
