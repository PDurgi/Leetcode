#User function Template for python3

import heapq
from typing import List
import collections

class Solution:
    def shortestPath(self, n: int, m: int, edges: List[List[int]]) -> List[int]:
        # Initialization
        queue = []
        start = 1
        heapq.heappush(queue, (0, start))  # Updated the heap element
        distance = [float('inf')] * (n + 1)
        distance[start] = 0
        parent = [i for i in range(n + 1)]  # Simplified the parent initialization
        path = []
        adj = collections.defaultdict(list)

        # Build adjacency list
        for edge in edges:
            source, dest, weight = edge
            adj[source].append((dest, weight))
            adj[dest].append((source, weight)) 

        # Dijkstra's algorithm
        while queue:
            source_dist, node = heapq.heappop(queue)  # Updated the unpacking
            for neighbour, dist in adj[node]:
                if dist + source_dist < distance[neighbour]:
                    distance[neighbour] = dist + source_dist
                    parent[neighbour] = node
                    heapq.heappush(queue, (distance[neighbour], neighbour))  # Updated the heap element

        # Reconstruct the path
        if distance[n] == float('inf'):
            return -1
        while parent[n] != n:
            path.append(n)
            n = parent[n]
        path.append(start)
        return path[::-1]



        

#{ 
 # Driver Code Starts

if __name__ == "__main__":
    for _ in range(int(input())):
        n,m = map(int,input().split())
        edges = []
        for i in range(m):
            a,b,c = map(int,input().split())
            edges.append([a,b,c])
        
        obj = Solution()
        res = obj.shortestPath(n, m, edges)
        for e in res:
            print(e,end=" ")
        print()
# } Driver Code Ends