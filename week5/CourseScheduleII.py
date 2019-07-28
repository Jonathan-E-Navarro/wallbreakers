from collections import defaultdict
import sys
class Solution:
    def __init__(self):
        self.graph = defaultdict(list)
        self.visited = set()
        self.stack = []
        self.top = []
        
    def check_cycle(self,node):
        self.visited.add(node)
        self.stack.append(node)
        for neighbor in self.graph[node]:
            if neighbor not in self.visited:
                if self.check_cycle(neighbor):
                    return True
            elif neighbor in self.stack:
                return True
        #pop off the recursion stack and add that element to our 
        #topological ordering list
        self.top.append(self.stack.pop())
        return False
    
    
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses == 0 or len(prerequisites) == 0:
            return [course for course in range(numCourses)]       
        for course,prereq in prerequisites:
            self.graph[course].append(prereq)
            
        for node in range(numCourses):
            #if we haven't already visited this node
            if node not in self.visited:
                #if a cycle is found
                if self.check_cycle(node):
                    return []
        #no cycles have been found, return True we can take all courses
        return self.top
        # print(self.graph)