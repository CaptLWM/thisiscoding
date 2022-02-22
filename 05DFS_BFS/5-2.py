from collections import deque
#큐 구현을 위해선 라이브러리 필요

queue = deque()

queue.append(5)
queue.append(4)
queue.append(3)
queue.append(2)
queue.popleft() # 5가 빠짐
queue.append(3)
queue.append(1)
queue.popleft() # 4가 빠짐
# queue.popright() 는 없음

print(queue)
queue.reverse()
print(queue)
