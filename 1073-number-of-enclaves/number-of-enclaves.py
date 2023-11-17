class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        #similar to surronded regions #leetcode 130
        #we will just count the number of non visited 1's that are not on boundary in this approach
        #lets use BFS traversal this time
        rows= len(grid)
        cols=len(grid[0])
        queue=collections.deque()
        no_of_land=0
        visited=[[0 for _ in range(cols)] for _ in range(rows)]
        #traversing the boundary of a matirix
        for j in range(cols):
            if grid[0][j] == 1 and visited[0][j] != 1:
                queue.append((0, j))
                visited[0][j] = 1
            if grid[rows - 1][j] == 1 and visited[rows - 1][j] != 1:
                queue.append((rows - 1, j))
                visited[rows - 1][j] = 1
        # first and last cols
        for i in range(rows):
            if grid[i][0] == 1 and visited[i][0] != 1:
                queue.append((i, 0))
                visited[i][0] = 1
            if grid[i][cols - 1] == 1 and visited[i][cols - 1] != 1:
                queue.append((i, cols - 1))
                visited[i][cols - 1] = 1
        #bfs traversal            
        directions=[(-1,0),(0,1),(1,0),(0,-1)]
        while(queue):
            row,col=queue.popleft()
            for direction in directions:
                dr=row+direction[0]
                dc=col+direction[1]
                if dr in range(rows) and dc in range(cols) and visited[dr][dc]==0 and grid[dr][dc]==1:
                    queue.append((dr,dc))
                    visited[dr][dc]=1
        for r in range(rows):
            for c in range(cols):
                if visited[r][c]==1 or grid[r][c]==0:
                    continue
                if grid[r][c]==1 and visited[r][c]==0:
                    no_of_land+=1
        return no_of_land