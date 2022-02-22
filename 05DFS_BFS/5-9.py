#BFS : 넓이 우선 탐색, 큐 구조, BFS 보단 속도가 조금 빠름

from collections import deque
import queue

#BFS 정의
def bfs(graph, start, visited):
    #deque 라이브러리 사용
    queue=deque([start])
    visited[start]=True
    #큐가 빌때가지 반복
    while queue:
        v=queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False]*9

bfs(graph, 1, visited)