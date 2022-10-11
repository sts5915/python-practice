#코딩테스트 (1. 백준(31%) 난이도가 있음 2. 프로그래머스(30%))
# 프로그래머스로 들어가서 문제풀어보기 깃허브로 가입하면 된다
# 문제 해결
#정수 num이 짝수일 경우
#"even"
#홀수인경우
#"Odd"
# 제한조건 num은 int범위의 정수
#0은 짝수

# def solution(num):
#     if num % 2 ==0:
#         answer = 'Even'
#     else :
#         answer = 'Odd'
#     return answer

# print(solution(3))
# print(solution(4))

# def sum(a,b):
#     return a+b

# a = input("입력하세요")
# b = input("입력하세요")
# print(sum(a,b))


# def sum(a,b):
#     return a+b  # return한 순간 함수는 끝났기 때문에 밑에 다른 함수가 들어가도 반영되지 않는다

# a = input("입력하세요")
# b = input("입력하세요")
# print(sum(a,b))


# 형변환
# def sum(a,b):
#     print(type(a))
#     print(type(b))
#     try:                       # 이것을 써서 오류를 짚어줄수 있다
#         if type(a) == int and type(b) ==int:
#             return a + b
#         else:
#             return int(a) + int(b)
#     except:
#         return f"{a}랑 {b}중 숫자가 아닌게 있습니다"
# a = input("입력하세요")
# b = input("입력하세요")
# print(sum(a,b))

# 계속 하고 싶을때
# def sum(a,b):
#     print(type(a))
#     print(type(b))
#     try:                       
#         if type(a) == int and type(b) ==int:
#             return a + b
#         else:
#             return int(a) + int(b)
#     except:
#         return f"{a}랑 {b}중 숫자가 아닌게 있습니다"
# a = input("입력하세요")
# b = input("입력하세요")
# print(sum(a,b))
# while True :
#     a = input("입력하세요")
#     b = input("입력하세요")
#     if a=="end" or b=="end":
#         break
#     print(sum(a,b))

# for in 을 쓰면 범위 지정이 되서 while과 조금 다르다



# 3,6,9게임 만들기
# 돌아온 숫자에 3.6.9
# c
# 지속되어야 하는 게임
# 369396 현재 1
#입력 다음 할것


# 내가 풀어서 틀린거
# while True:
#     a = input("369369 현재  ")
#     if type(a) == str :
#         return 
#     if a=="":
#         print("졌습니다")
#         break

#정답
# def game():

#     i=0
#     while True:
#         i+=1
#         myInput = input(f"현재 값 {i} ")
#         answer = str(i+1)
#         for c in str(i+1):
#             if c=="3" or c=="6" or c=="9":
#                 answer = "c"
#         if myInput == answer:
#             print("맞았다")
#         else :
#             print("game over")
#             break

# def game(cur,myInput):
#     answer = str(cur)
#     for c in str(cur):
#         if c=="3" or c=="6" or c=="9":
#             answer = "c"
#     if myInput == answer:
#         print("맞았다")
#         return True
#     else :
#         print("game over")
#         return False    
# i=0
# while True:
#     i+=1
#     myInput = input(f"현재 값 {i} ")
#     isWin = game(i+1, myInput)
#     if(not isWin):
#         break

# 뒤 4자리만 빼고 다 *
# input 번호 받아서 010-2222-2222
#뒷 4자리만 빼고 ***-****-2222
# 02-7777-8888 **-****-8888

#내가 푼것 틀린거
# def solution(phone_number):
#     answer = ''
#     for i in (0, len(phone_number)-4):
#         answer = "*" + phone_number
#         return answer
# print(solution("01033333333"))
# 
# 
# 정답
# 
# def solution(phone_number):
#     answer = ''
#     for i in range(0, len(phone_number)):
#         if i < len(phone_number)-4:
#             answer += "*"
#         else :
#             answer += phone_number[i]
#     return answer        
# print(solution("01022222222"))


# 중간에 -를 살릴때
def solution(phone_number):
    answer = ''
    for i in range(0, len(phone_number)):
        if i < len(phone_number)-4:
            if phone_number[i]=="-":
                answer +="-"
            else:
                answer += "*"
        else :
            answer += phone_number[i]
    return answer
print(solution("02-333-3333"))

# 이걸 보고 반대로 해석도 할 줄 알아야 한다




