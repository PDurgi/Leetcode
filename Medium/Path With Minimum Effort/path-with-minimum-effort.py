#User function Template for python3
import heapq
class Solution:
        
    def MinimumEffort(self, heights):
        #code here

        #we will use dijkstra's algorithm logic and a priority queue(min)
        # the only logic is we will look at the abs difference between cells
        #similar to binary maze problem 
        
        rows=len(heights)
        cols=len(heights[0])
        distance = [[float('inf') for _ in range(cols)] for _ in range(rows)]
        directions=[[-1,0],[1,0],[0,-1],[0,1]]
        queue=[]
        #push into PQ =>abs difference,(soure node i.e tuple(0,0)) 
        heapq.heappush(queue,(0,(0,0)))
        target=(rows-1,cols-1)
        result=0
        distance[0][0]=0
        while queue:
            difference,(row,col)=heapq.heappop(queue)
            if (row,col)==target:
                #once we get the target/destination it means that the priority queue has popped out min distance
                #the difference values being popped next will be only greater than the current value
                #i.e if difference is now 2, next popped values will be greater. therefore we return
                
                return difference
                
            for direction in directions:
                dr=row+direction[0]
                dc=col+direction[1]                
                if dr in range(0,rows) and dc in range(0,cols):
                    #A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.
                    abs_diff=max(abs(heights[row][col]-heights[dr][dc] ),difference)
                    if abs_diff < distance[dr][dc]:
                        distance[dr][dc]=abs_diff
                        heapq.heappush(queue,(abs_diff,(dr,dc)))
        return result
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n,m=map(int,input().split())
        a=[]
        for i in range(n):
            li=list(map(int,input().split()))
            a.append(li)
        ob = Solution()
        ans = ob.MinimumEffort(a)
        print(ans)
        tc -= 1
# } Driver Code Ends