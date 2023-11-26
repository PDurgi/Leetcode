import collections

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # we will solve this using Dijkstra's algorithm logic
        # since all nodes are located at unit distance we dont actually require a priority queue
        # standard BFS

        size=len(grid)
        if grid[0][0] !=0 or grid[size-1][size-1] !=0:
            return -1
        if grid[0][0]==0 and size==1:
            return 1
        queue=collections.deque([(1,(0,0))])
        #pushing distance, cell into the heap 
        #The length of a clear path is the number of visited cells of this path.
        target=(size-1,size-1)
        distance=[[float('inf') for _ in range(size)] for _ in range(size)]
        distance[0][0]=1
        directions=[[0,-1],[0,1],[1,0],[-1,0],[-1,1],[1,1],[-1,-1],[1,-1]]  
        while queue:
            dist,(row,col)=queue.popleft()
            if (row,col)==target:
                return dist
            for direction in directions:
                delta_r=row+direction[0]
                delta_c=col+direction[1]
                if delta_r in range(0,size) and delta_c in range(0,size):
                    if grid[delta_r][delta_c]==0:
                        if dist+1 < distance[delta_r][delta_c]:
                            distance[delta_r][delta_c]=dist+1
                            queue.append((dist+1,(delta_r,delta_c)))
 
        return -1
        