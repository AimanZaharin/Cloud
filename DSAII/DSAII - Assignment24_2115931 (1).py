
vertices = 4
infinite = 100000
 
def floydWarshall(graph):
 
    distance = list(map(lambda i: list(map(lambda j: j, i)), graph))
 
    for k in range(vertices):
        for i in range(vertices):
            for j in range(vertices):
                distance[i][j] = min(distance[i][j],
                                 distance[i][k] + distance[k][j])
    printSolution(distance)
 
def printSolution(distance):
    print("The output will be as the following matrix: ")
    
    for i in range(vertices):
        for j in range(vertices):
            if(distance[i][j] == infinite):
                print("%7s" % ("INF"), end=" ")
            else:
                print("%7d\t" % (distance[i][j]), end=' ')
            if j == vertices-1:
                print()
 
# Driver's code
if __name__ == "__main__":

    graph = [[0, 0, 4, 0],
             [1, 0, 6, 3],
             [0, 0, 0, 0],
             [infinite, 5, 1, 0]]
    
    floydWarshall(graph)