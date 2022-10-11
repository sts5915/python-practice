from human import Human


class Arm(Human):
    def __init__(self,side, name) -> None:
        print("팔")
        self.side = side
        super().setName = name # 끌어올때 기본적인것을 가져올때 __init__을 쓰지만 .으로는 직접적으로 변경시킬수 없기때문에
                               # 상위 함수에서 변형을 한번 줘서 그것을 가져와야 한다 그러면 .으로 가져올수있다
        pass