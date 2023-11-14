# SIMILAR TO TIME TAKES TO INFECT TREE
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        visited=set()
        time=0
        fresh_orange=0
        queue=collections.deque()   
        #count fresh oranges i.e grid val=1
        #we will also push all the rotten oranges to our queue     
        for i  in range(rows):
            for j in range(cols):
                if grid[i][j]==2:
                    queue.append((i,j))
                if grid[i][j]==1:
                    fresh_orange+=1
        directions=[(0, 1), (0, -1), (1, 0), (-1, 0)] # all four directions
        while(queue and fresh_orange>0):
            q_len=len(queue)
            for i in range(q_len):
                r,c = queue.popleft()
                for direction in directions:
                    delta_r=r+direction[0]
                    delta_c=c+direction[1] 
                    if delta_r in range(rows) and delta_c in range(cols): # index should be inside bounds
                        if (delta_r,delta_c) not in visited and grid[delta_r][delta_c]==1:
                            grid[delta_r][delta_c] = 2
                            fresh_orange-=1
                            queue.append((delta_r,delta_c))
                            visited.add((delta_r,delta_c))
            time+=1
        if fresh_orange==0:
            return time
        else: 
            return -1

                        


        