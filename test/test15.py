# 계산기를 만들어보자
# 기본적인 계산기

# def add(a,b):
#     return a+b

# def diff(a,b):
#     return a-b

# i=0
# i=add(i, 10)
# i=diff(i, 5)
# print(i)

# j=0
# j=add(j, 5)
# j=diff(j, 3)
# print(j)

# 여러개 할수있지만 너무 비효율적이다
# 이럴때 쓰는것이 class (함수들의 모음과 같다(일단))
# @overload 는 같은 이름인데 다른 기능을 할때 붙여준다

# class calculator: # calculator는 이름 부여
#     def __init__(self) -> None: #init은 초기값 설정
#         self.result =0
#     def add(self,b):
#         self.result += b
#     def diff(self,b):
#         self.result -= b    

# def 함수 Function
# result = 0
# result = result +10
# result = result -2
# print(result)



# 모듈 - 조립시에 적용하는 단위
# from test16 import calculator
#from this import d
#from arm import Arm
from cat import Cat
from dog import Dog
#from human import Human
#from leg import Leg
#from test17 import User
from test18 import Animal


# cal1 = calculator()
# cal1.add(10)
# cal1.diff(5)
# print(f"cal1\t{cal1.result}")

# cal2 = calculator()
# cal2.add(10)
# cal2.diff(2)
# print(f"cal2\t{cal2.result}")

# a = list()
# a.append(1)

# b = list()
# b.append(2)
# print(a)
# print(b)


# user1= User(id="bit", password="1234") # id= password= 는 안써도 된다
# user1.printUser()
# user1.change_id("pppp")
# user1.printUser()


# l=Leg("left", "park")
# print(l.side)
# print(l.name)
# l.setName("kim")
# print(l.name)

# an = Animal()
# print(an.name)
# an.__setattr__("name","?") #__했을때 나오는 목록중 보라색은 함수 파란색은 변수 따라서 함수뒤에 ()는 필수
# print(an.__dict__)


# Cat과 Dog에서 name을 따로 지정 안해줘도 Animal에서 지정을 해줘서 쓸수 있다
cat = Cat()
cat.printSound()
print(cat.type)
print(cat.butler)
print(cat.__dict__)

# 'type' : '고양이'
# 'sound' : '야옹'
# 'butler' : 'True'
# = Cat 위 세개를 다 갖고 있어야 Catㅇ이다
# 이 각각을 객체라고 하고 딕셔너리라고 한다 그래서 {}가 출력된다
# 이것을 객체 지향이라고 한다


dog=Dog()
dog.printSound()
print(dog.type)

# class는 하나의 물체를 만들기 위해 쓰고 
# 상속(더 상위개념에서 받아오는 개념)은 공통 코드를 줄이기 위해서 쓴다
# 객체 지향에 대해서는 자바에서 더 자세히 배우고 자바에서 더 많이 쓴다




































