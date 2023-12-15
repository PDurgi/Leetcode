import collections
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        #if we do a bfs if space complexity is not an issue
        
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


            

        
        
        
        