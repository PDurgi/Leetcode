class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #pre-req : Topological sort
        #if topological sort is possible ( there is no cycle) , we say that we can finish them
        indegree=[0]*numCourses
        queue=collections.deque()
        adj_list=collections.defaultdict(list)
        
        for prereq in prerequisites:
            adj_list[prereq[0]].append(prereq[1])
            indegree[prereq[1]]+=1
        for i in range(numCourses):
            if indegree[i]==0:
                queue.append(i)
        topo_sort=[]
        while queue:
            node=queue.popleft()
            topo_sort.append(node)
            for neighbour in adj_list[node]:
                #reduce the indegree of the neighbour
                indegree[neighbour]-=1
                if indegree[neighbour]==0:
                    #push into queue only if indegree==0
                    queue.append(neighbour)
        
        if len(topo_sort)==numCourses:
            return True
        return False
        