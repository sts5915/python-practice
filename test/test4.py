list = [1,2,3,4,5,6,2,3,5,1]
i=0
while i<len(list):
    if list[i]%2 == 0:
        print(f"{list[i]}는 짝수입니다")
    elif list[i]%2 == 1:
        print(f"{list[i]}는 홀수입니다")
    i+=1