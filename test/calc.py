# 정적 변화가 없다

from typing import overload


class Calc:
    @staticmethod            #@는 어노테이션(용어니까 외우자) 선언을 하면 self가 생기고 안하면 self가 없다
    def add(a,b):            #하면 앞자리는 무조건 self자리가 된다 안주면 그냥 변수
        print(a,b)
    @staticmethod
    # @overload
    def diff(s,a,b):
        print(a+b)
    @staticmethod
    # @overload            # 같은 이름인데 다른 함수일때 붙여준다
    def diff(s,a):
        print(a+s)
    
print("test");
