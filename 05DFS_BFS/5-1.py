#스택예제
stack=[]
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop() #데이터 꺼내기 => 7 꺼냄
stack.append(1)
stack.append(4)
stack.pop() #데이터 꺼내기 => 4 꺼냄

print(stack)
print(stack[::-1])