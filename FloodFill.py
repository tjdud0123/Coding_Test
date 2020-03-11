from collections import deque

def visitable(n, m, x, y, visited):
    return 0 <= x < n and 0 <= y < m and not visited[x][y]

def bfs(n, m, x, y, image, visited):
    Deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    temp = deque([(x, y)])
    
    while temp:
        cur_x, cur_y = temp.popleft()
        for dx, dy in Deltas:
            next_x, next_y = cur_x + dx, cur_y + dy
            if visitable(n, m, next_x, next_y, visited) and \
            image[cur_x][cur_y] == image[next_x][next_y]:
                temp.append((next_x, next_y))
                visited[next_x][next_y] = True
    

def solution(n, m, image):
    visited = [[False] * m for _ in range(n)]
    answer = 0
    
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                visited[i][j] = True
                answer +=1
                bfs(n, m, i, j, image, visited)
    
    return answer