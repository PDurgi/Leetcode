#we will do a dfs check
# a terminal node returns False on dfs check, if it returns false we will append it to result
#pre-req - find cycles in a directed graph using dfs 
#every node connected to cycle cannot be a safe node
#every node incoming/leading to cycle cannot be a safe node

from typing import List
import collections

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        size=len(graph)
        visited = [0] * size
        path_visited = [0] * size
        safe_nodes=[0] * size
        result=[]
        def dfs_check(vertex,visited,path_visited,safe_nodes):
            visited[vertex] = 1
            path_visited[vertex] = 1
            safe_nodes[vertex]=0
            for neighbour in graph[vertex]:
                if visited[neighbour] == 0:
                    if dfs_check(neighbour,visited,path_visited,safe_nodes):
                        return True
                elif path_visited[neighbour] == 1:
                    return True
            safe_nodes[vertex]=1
            path_visited[vertex] = 0
            
            return False
        for vertex in range(len(graph)):
            if visited[vertex] == 0:
                dfs_check(vertex,visited,path_visited,safe_nodes) 
        
        for i in range(len(safe_nodes)):
            if safe_nodes[i]==1:
                result.append(i)
        return result