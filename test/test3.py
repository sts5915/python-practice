# list = [1,2,3,4,5,6,2,3,5,1]
# 뭐는 짝수입니다
# 뭐는 홀수입니다
# 35 분에 카톡
list1 = [1,2,3,4,5,6,2,3,5,1]
re=0
# for el in list1:
#    print(el)
#    if el % 2 ==0:
#        print(f"[el] 은 짝수 입니다")
#    elif el % 2 ==1:
#        print(f"[el] 은 홀수 입니다")
i=0
while i<len(list1):
    if list1[i] % 2 == 0:
        print(f"{list1[i]} 은 짝수 입니다")
    elif list1[i] % 2 == 1:
        print(i)
        # print(f"{list1[i]} 은 홀수 입니다")
        continue # 반복문, break는 반복문이 끝남
    i+=1
    # print(f"---------{list1[i]}---------------")
        
        
    