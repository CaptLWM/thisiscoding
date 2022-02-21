#게임개발
#캐릭터가 있는 장소는 N x M 직사각형 (한칸 1)
#캐릭터는 동 서 남 북 중 한곳을 바라봄
#맵 각 칸은 A,B로 나타낼 수 있고
# 이동 규칙
#     1. 현재 방향을 기준으로 왼쪽부터 차례대로 갈곳을 정함
#     2. 캐릭터 바로 왼쪽에 가보지 않은 칸이 있다면, 왼쪽으로 회전한 다음 왼쪽으로 한칸 전진
#         가보지 않은 칸이 없다면, 왼쪽 방향으로 회전만 수행하고 1단계로 돌아감
#     3. 만약 네 방향 모두 이미 기본칸이거나 바다로 되어 있는 칸인 경우, 바라보는 방향을 유지한채로 한칸 뒤로 가고 1단계로
#         단, 뒤쪽이 바다칸인 경우 움직임을 멈춤

n, m = map(int, input().split())

#방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]
# _ 는 사용되지 않을 더미데이터 사용할 때 사용

# 현재 캐릭터의 좌표, 방향 입력받기
x,y,direction = map(int, input().split())
d[x][y] = 1 # 현재 좌표 방문 처리

# 전체 맵 정보를 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))
    #list 형식으로 array에 붙여넣기

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction # direction 변수 사용하기 위해(전역변수) global 사용
    direction -= 1
    if direction == -1:
        direction = 3

#시뮬레이션 시작
count = 1
turn_time = 0
while True:
    #왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0: #x, y 이동이 없으면 0이 곱해질 거기 때문
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time =0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time +=1
    # 네방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        #뒤로 가기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        #뒤가 바다로 막힌 경우
        else:
            break
        turn_time = 0
#정답 출력
print(count)