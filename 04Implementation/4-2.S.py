#왕실 나이트
#왕실 정원은 8*8 좌표평면 / 한칸에 나이트 있음
#나이트 이동 경우의 수
# 1. 수평으로 두칸 이동 후 수직으로 한칸
# 2. 수직으로 두칸 이동 후 수평으로 한칸

input_data = input()
#행
a=int(ord(input_data[0]))-int(ord('a'))+1
#열
b=int(input_data[1])

# 이동할 수 있는 방향 정의
steps=[(-2,1),(-2,-1),(-1,2),(-1,-2),(1,2),(1,-2),(2,1),(2,-1)]

result=0
for step in steps:
   next_a = a+step[0]
   next_b = b +step[1]
   if next_a>=1 and next_a <=8 and next_b >=1 and next_b<=8:
       result += 1
print(result)