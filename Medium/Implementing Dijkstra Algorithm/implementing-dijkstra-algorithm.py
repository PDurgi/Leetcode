import heapq
import collections
class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):

        queue=[]
        heapq.heappush(queue, (S,0))
        distance=[float('inf')]*V
        distance[S]=0
        while queue:
          node,source_dist=heapq.heappop(queue)
          for neighbour,dist in adj[node]:
 
            if dist + source_dist < distance[neighbour]:
                distance[neighbour]=dist + source_dist
                heapq.heappush(queue, (neighbour, distance[neighbour]))
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