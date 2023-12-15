import collections
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        adj_list=collections.defaultdict(list)
        queue=collections.deque()
        for path in paths:
            adj_list[path[0]].append(path[1])
        queue.append(paths[0][0])
        destination=None
        while queue:
            node=queue.popleft()
            for neighbour in adj_list[node]:
                queue.append(neighbour)
        return node


            

        
        
        
        