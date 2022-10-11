# main
# main 은 내가 실행시킬 것 (java에서 많이 쓰인다)
# java는 무조건 main start

#package 묶음 
from calc import Calc
# from calculator.add import add
# from calculator.diff import diff
# from person import Person
# from test4.input import testInput    # 다른 폴더에 있는것을 끌어올때 __init__.py 없을때 package가 아니라고 오류가 난다 
# from user.age import showAge
# from user.name import showName  


def main():
    # count = 0
    # count = add(count, 4)
    # count = diff(count, 10)
    # print(count)    # -6
    # text =testInput()    
    # print(text)
    # showName("park")
    # showAge(21)
    # a=Person()
    # Person.count += 1 count = 1
    # self.count += 1   count = 2
    # b=Person()
    # Person.count += 1 count = 2
    # self.count += 1   count = 3
    # c=Person()
    # Person.count += 1  count = 3
    # self.count += 1    count = 4
    # print(a.count)
    # print(b.count)
    # print(c.count)
    # print(a.__dict__) # class에서 __dict__를 가져온것
    # print(b)
    # print(c.count)
    Calc.add(1,3)
    Calc.diff(1,3,1)

main()




