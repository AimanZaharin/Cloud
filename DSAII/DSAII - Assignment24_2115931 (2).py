from collections import defaultdict

class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def SET(self, n, v):
        self.graph[n].append(v)

    def FIND(self, parent, x):
        
        if parent[x] == x:
            return x
        
        if parent [x] != x:
            return self.FIND(parent, parent[x])
    
    def UNION(self, parent, x, y):
        parent[x] = y
    
    def isaCycle(self):
 
        parent = [0]*(self.V)
        for i in range(self.V):
            parent[i] = i
 
        for i in self.graph:
            for j in self.graph[i]:
                x = self.FIND(parent, i)
                y = self.FIND(parent, j)
                if x == y:
                    return True
                self.UNION(parent, x, y)

g = Graph(5)
g.SET(0, 2)
g.SET(4, 2)
g.SET(3, 1)
 
if g.isaCycle():
    print("This Graph has a cycle")
else:
    print("This Graph does not contain a cycle ")