
class Solution:
        #every adj node has diff color
        #linear graphs with no cycles are always bipartite
        #any graph with even cycle length can also be bipartite
        #at any moment we find out that the adj nodes have same color, we return a false
    def isBipartite(self, graph: List[List[int]]) -> bool:
        coloured = [-1] * len(graph)
        adj_list = collections.defaultdict(list)
        
        for i in range(len(graph)):
            adj_list[i] += graph[i]
            
        queue = collections.deque()
        
        for i in range(len(graph)):
            if coloured[i] == -1:
                queue.append((i, False))  # Start with the first uncolored node
                coloured[i] = False
        
                while queue:
                    node, node_color = queue.popleft()
                    
                    for neighbour in adj_list[node]:
                        if coloured[neighbour] == -1:  # Not yet colored
                            queue.append((neighbour, not node_color))
                            coloured[neighbour] = not node_color
                        elif coloured[neighbour] == node_color:
                            return False  # Neighbour has the same color as the current node
            
        return True
