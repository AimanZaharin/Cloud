def main():

    graph = [[0, 1, 0, 1, 0, 0],
             [0, 0, 0, 0, 1, 0],
             [0, 0, 0, 0, 1, 1],
             [0, 1, 0, 0, 0, 0],
             [0, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 0, 1]]
    

def warshall(graph):

    for k in range(1, n+1):

        for i in range(1, n+1):

            for j in range(1, n+1):

                p[i][j] = max(p[i][j], p[i][k] and p[k][j])



    


