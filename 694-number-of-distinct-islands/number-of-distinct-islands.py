class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        #extension to no.of islands problem
        #solving this using dfs
        #store the shape of island into a set and return the len of set
        islands=set()
        rows=len(grid)
        cols=len(grid[0])
        visited= [[0 for _ in range(cols)] for _ in range(rows)]
        def dfs(row,col,basex, basey):
            if (row not in range(rows) or
                col not in range(cols) or
                visited[row][col]==1 or
                grid[row][col]==0):
                return
            visited[row][col]=1
            island.append((row-basex,col-basey))
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for direction in directions:
                dr=row+direction[0]
                dc=col+direction[1]
                dfs(dr,dc,basex,basey)   

        for i in range(rows):
            for j in range(cols):
                if visited[i][j]==0 and grid[i][j]==1:
                    x,y = i,j
                    island=[]
                    dfs(i,j,x,y)
                    if len(island)>0:
                        islands.add(tuple(island)) #since list is mutable, convert to frozenset or tuple
        return len(islands)
        

        