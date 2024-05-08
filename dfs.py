from collections import defaultdict

class Graph:
    # Constructor
    def __init__(self):
        # default dictionary to store graph
        self.graph = defaultdict(list)
        
    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
        
    def DFSUtil(self, v, visited):
        visited.add(v)
        print(v, end=' ')
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)

    # The function to do DFS traversal.
    def DFS(self, v):
        # Create a set to store visited vertices
        visited = set()
        # Call the recursive helper function to print DFS traversal
        self.DFSUtil(v, visited)

# Create a graph
g = Graph()
print("Following is DFS starting from vertex 0")
g.DFS(1)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
