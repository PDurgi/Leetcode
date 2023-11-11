from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.adj_list = {}
        province = 0
        self.visited = [0] * len(isConnected)
        # Build the adjacency list
        for i in range(0,len(isConnected)):
            for j in range(0,len(isConnected[0])):
                if isConnected[i][j] == 1 and i != j:
                    self.addEdge(i, j)

        for i in range(0,len(self.visited)):  # Removed +1 from the range
            if self.visited[i] == 0:
                province += 1
                self.dfsUtil(i)
        return province
    def dfsUtil(self, root):
        self.visited[root] = 1
        for neighbor in self.adj_list.get(root, []):
            if self.visited[neighbor] == 0:
                self.dfsUtil(neighbor)
    def addEdge(self, source, dest):
        if source not in self.adj_list:
            self.adj_list[source] = []
        self.adj_list[source].append(dest)
        if dest not in self.adj_list:
            self.adj_list[dest] = []
        self.adj_list[dest].append(source)



    
        