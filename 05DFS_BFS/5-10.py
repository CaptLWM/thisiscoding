#N,M 을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

#2차원 리스트의 맵 정보 입력받기
graph=[]
for i in range(n):
    graph.append(list(map(int, input())))

#DFS 로 특정한 노드를 방문한 뒤에 연결된 모든 노드들 방문
def dfs(x,y):
    # 주어진 값 벗어나면 종료
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    
    #현재 노드를 방문 안했을때
    if graph[x][y] == 0:
        #현재 노드 방문처리
        graph[x][y] = 1
        #모든 방향에 대해 모두 재귀적으로 호출
        dfs(x, y-1)
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

#음료수 채우기
result=0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result+=1

print(result)