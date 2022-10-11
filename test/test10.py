# 함수

# def = define 정의

# 파이썬은 절차지향 무조건 한줄씩한줄씩 읽는다
# 자바는 객체지향(opp)

# isPrimary = True   cammel case 중간에 대문자를 쓰는 경우 한눈에 알아보기 편하게 하기 위해서
# is_primary_key = True snake case 언더바를 쓰는 경우 이것도 알아보기 편하게 하기 위해서
# 위 두 경우는 회사마다 다르게 쓴다

# def sum(a,b): # def sum을 정의한다 a,b는 매개변수
#     return a+b  #return은 반환 함수에 대입했을때 나오는 결과

# print(sum(1,2))   #sum(1,2)는 1,2는 인수 sum은 남들도 알아보기 쉽게 하기 위해서
# print(sum(3,5))

# def sum1():
#     return 2+2
# print(sum1())
# print()

#argument 매개변수
from ast import Num


def sum2(*args):  # *이 붙으면 여러개를 할 수있다
    print(args)
    pppp=0
    for arg in args:
        pppp+= arg
    return pppp

print(sum2(1,1,1,1,1,2))

def printFunc(**kwargs): # 딕셔너리준것 **는 딕셔너리 *는 여러개를 쓸수있다
    print(kwargs)
printFunc(a=1, b=1)



def makeHuman(name, age):
    return{"name" : name, "age" : age}
human1=makeHuman("kim", 30)
human2=makeHuman("park", 34)
print(human1)
print(human2)



def isPrimaryNumber(num):
    # for i in range(2, 31) :
    isPrimary = True  # 소수인가? 라는 질문
    # i=2 2<=j<2
    for j in range(2,num):
        if num % j ==0 :
            isPrimary = False
            break
    if isPrimary:
        return f"{num}은 소수입니다"
    else:
        return f"{num}은 소수가 아닙니다"
print(isPrimaryNumber(6))

# isPrimaryNumber(2,3,4,5)
def isPrimaryNumbers(*nums):  # *이 들어오면 for부터 시작하자
    for num in nums :
        isPrimary = True  
        for j in range(2,num):
            if num % j ==0 :
                isPrimary = False
                break
        if isPrimary:
            print(f"{num}은 소수입니다")
        else:
            print(f"{num}은 소수가 아닙니다")

isPrimaryNumbers(9,4,2,11,16) # print를 안붙이는 이유는 return이 없기 때문이다


name = "park"    #전역변수 함수 밖에 지정되어 있는것
name1 = "lee"       #전역변수
def setName1(name): # 매개변수
    print(f"2.{name}")  #kim
    # name1=name  # 지역변수  함수 안에서 선언한것
    # name=name   # 지역변수
    pppp=name     # 지역변수
    print(f"3.{name},{pppp}, {name1}")   #kim
    print(f"5.{name1}")
print(f"1.name1 : {name1}")
print(f"1.{name}")
setName1("kim")     # 인자값
print(f"4.{name}")   
print(f"2.name1 : {name1}")





