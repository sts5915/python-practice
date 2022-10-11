# 4. 정수 제곱근 판별
# n이 양의 정수 x의 제곱이라면 (x+1)의 제곱을 리턴
# n이 양의 정수 x의 제곱이 아니라면 -1을 리턴


def solution(n):
    answer = 0
    x = n ** 0.5
    if x == int(x):
        answer = (x+1)**2
    else :
        answer = -1
    return answer
print(solution(2560000))

def solution(n):
    answer = 0
    for i in range(1,n):
        if i * i == n:
            answer = i
            break
        elif i * i > n:
            break
    if answer == 0:
        return -1
    return (answer+1)*(answer+1)
print(solution(123))

