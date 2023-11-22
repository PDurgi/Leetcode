from collections import defaultdict
from queue import Queue
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        n = len(words)
        adj = {c:set() for w in words for c in w}
        q = Queue(maxsize=0)
        indegree = defaultdict(int)
        for i in range(n-1):
            minLen = min(len(words[i]), len(words[i+1]))
            w1, w2 = words[i], words[i+1]
            if w1[:minLen] == w2[:minLen] and len(w1) > len(w2): return ""
            
            for j in range(minLen):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break
        
               
        # kahan's algorithm for topological sort
        for u in adj.keys():
            if indegree[u] == 0:
                q.put(u)
        
        res = ""
        while not q.empty():
            u = q.get()
            res += u
            for v in adj[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    indegree.pop(v)
                    q.put(v)
                    
        if len(res) != len(adj):
            return ""
        return res