class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = {}
        #find a non empty vertex in the graph 
        for vertex in range(len(graph)):
            stack = []
            if vertex not in visited:
                stack.append(vertex)
                visited[vertex] = "blue"
                print("color: ",visited)
                #commmence DFS, every vertex will color its unseen neighbors the other color
                #if we come across a node that we've already seen and its color is the same as the current
                #vertex that it was tied to, then we can't produce a two coloring 
                while stack:
                    vertex = stack.pop()
                    for neighbor in graph[vertex]:
                        if neighbor not in visited:
                            stack.append(neighbor)
                            visited[neighbor] = "red" if visited[vertex] == "blue" else "blue"
                            
                        elif visited[neighbor] == visited[vertex]:
                            return False
        #return true if all went well or the graph was empty 
        return True