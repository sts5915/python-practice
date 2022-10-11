# 코딩테스트 난이도 1
# 2부터 30까지 소수 리스트 뽑아내기



answer=[]
for i in range(2, 31) :
    isPrimary = True  # 소수인가? 라는 질문
    # i=2 2<=j<2
    for j in range(2,i):
        if i % j ==0 :
            isPrimary = False
            break
    if isPrimary:
        answer.append(i)
print(answer)
            
    

        
        
    
    
    


# 구구단 만들기

# 2*1=2 .....
# 2단 만들기
# num=2
# for i in range(2,10):
#     for num in range(1,10)
#     print(f"{num}*{i}={num*i}")




#별 찍기
#*
#**
#***
#****
# text="*"
# for i in range(1,6):
#     st = ""
#     for j in range(1,i):
#         st=text*j
#     print(st)
