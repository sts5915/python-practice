# 1. 자연수 뒤집어 배열로 만들기


def solution(n):
    answer =[]
    answer=list(str(n))
    answer.reverse()
    for el in range(0, len(answer)):
        answer[el]=int(answer[el])
    return answer

print(solution(12414214124))

def solution(n):
    answer = []
    arr = list(str(n))
    arr.reverse()
    for el in range(0, len(arr)):
        answer.append(int(arr[el]))
    return answer
print(solution(123))

def solution(n):
    answer = []
    strA = str(n)
    for i in range(len(strA),0,-1):  # 범위를 반대로도 돌릴수 있다 항상 0부터 시작하는것이 아니다
        answer.append(int(strA[i-1]))
    return answer
print(solution(1234))

