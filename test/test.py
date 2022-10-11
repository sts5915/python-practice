# 제어문
a=10
b=5
# print(f"a>b {a>b}=True 크다 False 작다")
# : 뒤에는 무조건 띄어쓰기

if a > b :
    # 조건이 True 면 아래 문장을 실행한다
    print("")
    print(f"a > b 크다")
elif a < b:
    # elif 위의 조건이 아니면(False) 이걸 실행
    print(f"a > b  작다")
else: # else    if도 False elif False 다 아니면 실행
    print(f"a = b 같다")


c=[1,2,3]
# len(c)=3
if len(c)>3:
    print(c[0])
if len(c)>2:
    print(c[0])


