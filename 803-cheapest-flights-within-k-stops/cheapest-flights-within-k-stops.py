import collections
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        #this problem can be solved with a Priority Queue and Dijkstra's algo
        #We will do same dijsktra's but based on stops
        #along with price/distance array we will have a stops array
        
        adj=collections.defaultdict(list)
        for flight in flights:
            adj[flight[0]].append((flight[1],flight[2]))
        queue=[]
        heapq.heappush(queue,(0,src,0))
        price=[float('inf') for _ in range(n)]
        stops=[float('inf') for _ in range(n)]
        price[src]=0
        stops[src]=0
        while queue:
            source_price,node,curr_stops=heapq.heappop(queue)
            if node==dst:
                    return source_price
            if curr_stops>k:
                continue
            for neighbour,cost in adj[node]:
                nextstops=curr_stops+1
                if cost+source_price<price[neighbour] or nextstops < stops[neighbour]:
                    price[neighbour]=cost+source_price
                    stops[neighbour]= nextstops
                    heapq.heappush(queue,(cost+source_price,neighbour,nextstops)) 
                
        if price[dst]==math.inf:
            return -1
        return price[dst]