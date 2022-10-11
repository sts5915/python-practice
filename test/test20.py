# 복습
# MySQL, NoSQL, 
# 자바, 파이썬같은거 
# hadoop   데이터처리
# 웹프론트 백엔드   (java, javascript, pyhton)
# 머신러닝 딥러닝 텐서풀로  (12/ 14 시작 python)
# MySQL, NoSQL, DB
# DB란 저장소
# a=0
# a+=10
# a+=100
# 파이썬 개요 무슨 언어인가?
# 절차 지향
# type 
# 숫자 int 문자 str 리스트 list -> set tuple dict
# 각각 선언 방법
# a = 1
# a = "str"
# a = []
# a = {} set
# a = () tuple
# a = {key:value} dict
# 동적 타이핑이라고 한다
# 장점 : 타입을 지정 안해도 괜찮다
# 단점 : 오류 발생가능

# 스크립트 언어
# 소스 코드를 한줄씩 읽어서 곧바로 실행
# python 문법으로 코드를 작성했는데
# 컴퓨터 언어는 0,1이다
# 이거를 컴파일(python언어를 컴퓨터 언어로 바꾸는것)
# 따로 컴퓨터 언어로 바꿔서 따로 파일을 만들어서 그것을 실행하지 않고
# 바로 실행된다
# 
# 플랫폼 독립적 : os 상관없다(window mac, linux같은거)


# 제어문
# if, elif, else
# match, case  

# 반복문
# for in :
# while :
# break continue
# 람다(map, reduce, filter)

# from functools import reduce


# list1 = [9,1,2,4,3]
# def sum(x,y):
#     print(f"{x} {y}") #format
#     return x+y
# a = reduce(lambda x,y : sum(x,y),list1)

# user = {"id":"id","pass":"pass","name":""} 
# names = ["kim", "lee", "park"]
# namelist = list(map(lambda x : {"id":"id","pass":"pass","name":x,"age":30},names))
# print(namelist)

# finduser = list(filter(lambda x : x.get("name")=="park",namelist))
# print(finduser)
# avgAge = reduce(lambda x,y : x+y.get("age"),namelist,0)
# print(avgAge/len(namelist))


# 함수
# def :
# def sum(a,b): a,b 매개변수
#   return a+b
# sum(1,2) 1,2 인수

# def sum(*a): *a tuple
# sum(1,2,3,4)
# def sum(**a): **a dict
# sum(name=kim,age=56)



# name = "kim"  전역 변수
# def printName(name):
#   name = "lee"  지역 변수

# 파일 입출력
# f = open(파일, mode, )
# encoding UTF-8 한글

# 입력받고 싶을때 : input

# class
# 왜 씀? 반복작업 중복되는 것을 한번에 처리하기 위해서
# 객체 지향 
# class name :

# class name(상속) :

#   def __init__ : 필수
# 상속 접근 할때 super()
# def __init__(self):
# self 는 자신

# 정규식 개념 search match
# park@gmail.com
# 이거 이메일이 형식이 맞는지 보는것
# import re


# import 다른곳에서 불러올때 쓰인다
# import random

# from datetime import date
# print(date.today())    오늘 날짜

# c:\test -> c:\test\test2
# 상대 경로
# ./test2
# .. 상위 폴더
# 절대 경로
# c:\test\test2


def adder(a,b):
    if a > b :
        a,b=b,a
    return sum(range(a,b+1))

print(adder(20,20))



































