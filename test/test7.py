# 반복문
# while for
# for i in range(0,3) : # i는 index의 약자
#     print(1)


# list1 = ["a","b","c"]
# for i in range(0, len(list1)) :
#     print(list(i))

# for el in list1:
#     print(el)


# i=0
# while i < len(list1):
#     print(list1[i])
#     i+=1
# break continue
# list1 = [9,4,2,1,6,7,4,3,7]
# 만약에 홀수면 2배 짝수면 그냥의 리스트 만들고
# 만약 합이 20이 넘으면 끝




# list1 = [9,4,2,1,6,7,4,3,7]
# list2 = []
# i=0
# sum1=0
# while i < len(list1):
#     sum1 += list1[i]
#     if list1[i] % 2 == 1:
#         list2.append(list1[i]*2)
#     else :
#         list2.append(list1[i])
#     i+=1
#     if sum1 > 20:
#         break
# print(list2)




list1 = ["안", "녕", "하", "세", "요"]
i=0
hi=""
#while i < len(list1):
#    hi += list1[i]
#    i+=1
#print(hi)

# while 조건이 true인 동안 아래를 실행함
# for in range()
#for i in range(0, len(list1), 3):
#    hi += list1[i]
#print(hi)
#print(list1[3])
for el in list1:
    hi = hi + el
print(hi)