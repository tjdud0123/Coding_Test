def solution(m, n, puddles):
    
    if m == 1 or n == 1:
        return 0 if puddles else 1
    
    puddles = set([(y-1, x-1) for x, y in puddles])
    dist = [[1] + [0] * (m-1) for _ in range(n)]
    dist[0] = [1] * m

    for x, y in puddles:
        if x == 0 :
            for i in range(y, m):
                dist[0][i] = 0
        if y == 0 :
            for i in range(x, n):
                dist[i][0] = 0
    
    for i in range(1, n):
        for j in range(1, m):
            dist[i][j] = 0 if (i, j) in puddles else dist[i-1][j] + dist[i][j-1]
                
    return dist[n-1][m-1] % 1000000007