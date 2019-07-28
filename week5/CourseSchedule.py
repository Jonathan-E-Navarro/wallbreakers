from collections import defaultdict 
class Solution:
    def __init__(self):
        self.graph = defaultdict(list)
        self.visited = set()
        self.stack = []
    def check_cycle(self,node):
        self.visited.add(node)
        self.stack.append(node)
        # print("node: ",node)
        # print("visited: ",self.visited)
        # print("stack: ",self.stack)
        # print("\n")
        for neighbor in self.graph[node]:
            if neighbor not in self.visited:
                if self.check_cycle(neighbor):
                    return True
            elif neighbor in self.stack:
                return True
        self.stack.pop()
        print("no cycle")
        return False
        
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses == 0 or len(prerequisites) == 0:
            return True       
        for course,prereq in prerequisites:
            self.graph[course].append(prereq)
            
        for node in range(numCourses):
            #if a cycle is found
            if self.check_cycle(node):
                print("cycle found")
                return False
        #no cycles have been found, return True we can take all courses
        return True
        # print(self.graph)
            