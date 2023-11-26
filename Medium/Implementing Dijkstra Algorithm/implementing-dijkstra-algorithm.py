import heapq
import collections
class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):

        queue=[]
        #push distance and node as (0, source)
        heapq.heappush(queue, (0,S))
        distance=[float('inf')]*V
        distance[S]=0
        while queue:
          source_dist,node=heapq.heappop(queue)
          for neighbour,dist in adj[node]:
 
            if dist + source_dist < distance[neighbour]:
                distance[neighbour]=dist + source_dist
                heapq.heappush(queue, (distance[neighbour], neighbour))
        return distance

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends
