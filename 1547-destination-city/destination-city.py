import collections
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        #brute force =>if we do a bfs if space complexity is not an issue
        
        # adj_list=collections.defaultdict(list)
        
        # for path in paths:
        #     adj_list[path[0]].append(path[1])
        # queue=collections.deque()
        # queue.append(paths[0][0])
        # destination=None
        # while queue:
        #     node=queue.popleft()
        #     for neighbour in adj_list[node]:
        #         queue.append(neighbour)
        # return node

        source_set=set()
        for path in paths:
            source_set.add(path[0])
        for path in paths:
            if path[1] not in source_set:
                return path[1]
            




            

        
        
        
        