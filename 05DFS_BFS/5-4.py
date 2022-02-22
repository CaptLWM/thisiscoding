#재귀함수 종료 조건
def recursive_function(i): #종료조건 설정을 위한 변수 i
    if i == 100:
        return
    print(i, '번 재귀함수', i+1 ,'번 재귀함수를 호출')
    recursive_function(i+1)
    print(i,'번 재귀함수 종료')

recursive_function(1)