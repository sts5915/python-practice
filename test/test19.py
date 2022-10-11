# 여러가지 모듈




#import calendar
#import math
#import numbers
import random
# import re
#import re
# import webbrowser


#print("3.141592") # 원주율
#print(math.pi) # 원주율이 출력된다

#calendar.prmonth(2022,10)
# webbrowser.open("https://naver.com")
#print(random.random()*11+1) # 0<=answer<1 *11하면 범위가 0<=answer<11이 된다 1<=answer<12가 된다

# 정규식
# reg=re.compile("[A-z0-9]{5,15}")    {}는 글자수 
# reg=re.compile("[0-9]{4,5}")
# id = "2ㅑㅑㅑㅑ2445"
# print(reg.match(id))  # 완전히 같아야 한다
# print(reg.search(id)) # 그 안에서 일치하는게 있는지 찾는다


# 회원가입할때
# 비밀번호에서 특수문자, 영대문자 포함, 아이디 중복검사 등등에서 쓰인다
# 장문의 글을 쓸때 어떤 단어를 찾거나 몇번 쓰였는지 알려고 할때 쓰인다

# AI 자연어 처리
# 나는 오늘 좋다. = 감정처리 같은것을 자연어 처리라고 한다

#이메일                                               #.com이나 .co.kr이 올수 있기때문에 {2,3}범위 준것이다
# reg = re.compile("([A-Za-z0-9]+@[A-Za-z0-9]+\.[A-za-z]{2.3})")
# print(reg.match("sts5915@naver.com"))

# check 정규식이라고 한다





# 퀴즈
# 로또 1~45 
# 중복없이 
# 6자리 
# 5개 뽑자

#random
#lotto

# lotto=[]
# for i in range(0,6):
#     numbers = []
   
#     while len(numbers)<6:
#         num = int(random.random()*45+1)
#         tmpnumber = numbers.copy()
#         tmpnumber.append(num)
#         setNumbers = set(tmpnumber.copy())
#         if len(setNumbers) == len(tmpnumber):
#             numbers.append(num)
#     lotto.append(numbers)
# for text in lotto:
#     print(text)


# reg = re.compile("([0-9]{3}-[0-9]{3,4}-[0-9]{4})")
# phone_number = "010-2222-3333"
# print(reg.match(phone_number))

lottopaper=[]
for i in range(6):
    lotto=set()
    while len(lotto)<6:
        number = int(random.random()*45+1)
        lotto.add(number)
    lottopaper.append(lotto)

print(lottopaper)
    











