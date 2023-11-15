class Solution:
    #similar to flood fill, just update the matrix with bfs step
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        #do a BFS from each 0 and we will cover all ones at distance 1
        # second BFS will cover all ones at distance 2 and so on until the grid is completed
        rows=len(mat)
        cols=len(mat[0])
        visited=set()
        distance=0
        queue=collections.deque()    
        distance_mat=[[0 for _ in range(cols) ]for _ in range(rows)]  
        for i  in range(rows):
            for j in range(cols):
                if mat[i][j]==0:
                    queue.append((i,j))
                    visited.add((i,j))
        directions=[(0, 1), (0, -1), (1, 0), (-1, 0)] # all four directions
        while(queue):
            q_len=len(queue)
            for i in range(q_len):
                row,col=queue.popleft()
                distance_mat[row][col]=distance
                for direction in directions:
                        delta_r=row+direction[0]
                        delta_c=col+direction[1] 
                        if delta_r in range(rows) and delta_c in range(cols): # index should be inside bounds
                            if (delta_r,delta_c) not in visited and mat[delta_r][delta_c]==1:
                                queue.append((delta_r,delta_c))
                                visited.add((delta_r,delta_c))
            distance+=1

        return distance_mat
                

        