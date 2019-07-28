import sys
from collections import defaultdict
class Solution:
    def __init__(self):
        self.graph = defaultdict(list)
        self.distances = {}
        
    def search(self,vertex,dist_so_far):
        #if current path distance so far is larger than 
        #the previous recorded distance to this vertex, ignore it 
        #we care about critical path, largest distance from our first node 
        #to any node since this will be the shortest amount of time in which 
        #all nodes have recieved transmission. 
        if dist_so_far >= self.distances[vertex]:
            return
        else:
            self.distances[vertex] = dist_so_far
        
        for distance,neighbor in sorted(self.graph[vertex]):
            self.search(neighbor,distance+dist_so_far)
            
            
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        #construct graph use default dict 
        #so we dont have to worry about if there's a created entry for a vertex 
        for time in times:
            node = time[0]
            dest = time[1]
            dist = time[2]
            self.graph[node].append((dist,dest))

        #construct distances 
        for vertex in range(1,N+1):
            self.distances[vertex] = sys.maxsize
        # print(self.distances)
        
        self.search(K,0) #start search from node K 
        # print(self.distances)
        
        max_distance = max(self.distances.values())
        #if maxsize is still in the dict, it means we weren't able to reach all nodes
        if max_distance < sys.maxsize:
            return max_distance
        return -1
        