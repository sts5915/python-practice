# 1. 자연수 뒤집어 배열로 만들기
# 2. 제일 작은 수 제거하기 
# 3. 두 정수 사이의 합 
# 4. 정수 제곱근 판별

# 아무나 나와서 찍어서 설명
# 점심 이후에 설명
# 
# 3. 두 정수 사이의 합 구하기
# a=3 b=5면 합은 12
# a=3 b=3이면 합은 3
# a=5 b=3이면 합은 12

# 3. 두 정수 사이의 합

def solution(a, b):
    answer = 0
    if a == b :
        answer = a
    elif a > b :
        for i in range(b, a+1):
            answer = answer + i
    else :
        for i in range(a, b+1):
            answer = answer + i
    return answer

print(solution(20, 10))


