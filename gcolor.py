class Graph: 
    # Class for the map/graph
    
    def __init__(self, edges, n): 
        # Constructor to initialize list
        self.adjList = [[] for _ in range(n)]
        for src, dest in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)
    
    def colorGraph(self, n):
        result = {}
        for u in range(n):
            assigned = set([result.get(i) for i in self.adjList[u] if i in result])
            color = 1
            for c in assigned:
                if color != c:
                    break
                color += 1
            result[u] = color
        
        for v in range(n):
            print(f"Color Assigned to vertex {v} is {colors[result[v]]}")

if __name__ == "__main__":
    colors = ['','BLUE','GREEN','RED','YELLOW','ORANGE','PINK','BLACK','BROWN']
    edges = [(0,1),(0,4),(0,5),(4,5),(1,4),(1,3),(2,3),(2,4)]
    n = 8
    graph = Graph(edges, n)
    graph.colorGraph(n)
