from typing import List
import collections

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # create adj list from dictionary and in_degree
        # create adj list from dictionary and in_degree
        n = len(words)
        adj = {c:set() for w in words for c in w}

        in_degree = defaultdict(int)
        for i in range(n-1):
            minLen = min(len(words[i]), len(words[i+1]))
            w1, w2 = words[i], words[i+1]
            if w1[:minLen] == w2[:minLen] and len(w1) > len(w2): return ""
            
            for j in range(minLen):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        in_degree[w2[j]] += 1
                    break

        
        queue=collections.deque()
        
        for vertex in adj.keys():
            if in_degree[vertex]==0:
                queue.append(vertex)
                
        ans=[]
        q=collections.deque([c for c in in_degree if in_degree[c]==0])
        while q:
            c=q.popleft()
            ans.append(c)
            for d in adj[c]: # c < d
                in_degree[d]-=1
                if in_degree[d]==0:
                    q.append(d)
        if len(ans) < len(in_degree):
            return ""   
        return ''.join(ans)