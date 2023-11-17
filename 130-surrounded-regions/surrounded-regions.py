class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # zero cannot be flipped if its on the boundary
        # Start from boundary Os, mark the boundary O's as cannot be modified and Convert the rest to X
        # DFS/BFS for traversal
        rows= len(board)
        cols=len(board[0])
        visited=[[0 for _ in range(cols)] for _ in range(rows)]

        def dfs(row,col,visited):
            if (row not in range(rows) or
                col not in range(cols) or
                visited[row][col]==1 or
                board[row][col]=='X'):
                return
            visited[row][col]=1
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for direction in directions:
                dr=row+direction[0]
                dc=col+direction[1]
                dfs(dr,dc,visited)
        #traversing on the boundary 
        #first and last rows
        for j in range(cols):
            if board[0][j]=="O" and visited[0][j]==0:
                dfs(0,j,visited)
            if board[rows-1][j]=='O'and visited[rows-1][j]==0:
                dfs(rows-1,j,visited)
        #first and last cols:
        for i in range(rows):
            if board[i][0]=='O'and visited[i][0]==0:
                dfs(i,0,visited)
            if board[i][cols-1]=='O'and visited[i][cols-1]==0:
                dfs(i,cols-1,visited)

        #mark the not visited ones as X in original matrix
        for row in range(rows):
            for col in range(cols):
                if visited[row][col]==1:
                    continue
                board[row][col]='X'
        
