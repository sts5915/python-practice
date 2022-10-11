class Person:
    count = 0
    def __init__(self) -> None:
        Person.count += 1 # -> 3,3,3 한번 실행하면 전부 실행되는것 
        # self.count += 1 -> 1,1,1 각각 개별이다

    # def __dict__(self):             이것을 안써도 자동적용된다(그래서 main파일의 dict를 쓸수 있는것)
    #     return{"count":""}

        