class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #pre-req : Topological sort
        #if topological sort is possible ( there is no cycle) , we say that we can finish all courses
        # if topo sort is not possible then len(topo array)  will not be equal to number of nodes

        indegree=[0]*numCourses
        queue=collections.deque()
        adj_list=collections.defaultdict(list)
        
        for prereq in prerequisites:
            adj_list[prereq[1]].append(prereq[0])
            indegree[prereq[0]]+=1
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
            return topo_sort
        return []       