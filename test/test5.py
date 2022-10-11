# from functools import reduce
# import pstats


# list1 = [1,2,3,4,5,6,2,3,5,1]
# for el in list1:
    #match el%2:
        #case 1:
            #print(f"{el}은 홀수 입니다")
        #case 0:
            #print(f"{el}은 짝수 입니다")

# 람다 버전 3.6부터 지원
# 예제) list1의 요소를 *2해서 찍어봐라
# for i in list1:
#    list2.append(i*2)
# print(list2) 

# list4 = list(map(lambda x: x*2, list1))
# print(list4)
# map은 새로운 리스트를 만든다

# tmpd = {"name": "re", "age":100}
# list5 =[tmpd,tmpd,tmpd]
# list6 = list(map(lambda el: el.copy(), list5))
# list7 = list5.copy()
# print(list5)
# print(list6)
# print(list7)
# list5.append(1)
# print()
# print(list5)
# print(list6)
# print(list7)
# tmpd["age"]=10
# print()
# print(list5)
# print(list6)
# print(list7)



#list1 요소의 합 ? int(수)
# list1 = [1,2,3,4,5,6,2,3,5,1]
# sum=0
# for el in list1 :
#     sum += el    #sum = sum + el
# print(sum)

# sum2 = reduce(lambda x,y:x+y, list1)
# # 합계 구할때 쓴다
# print(sum2)

list1 = [1,2,3,4,5,6,2,3,5,1]
list0 = []
# 4 이상인 것만 리스트를 만들어보자
# 4 이상인 것 만 (조건)
# for el in list1:
#     # print(el)
#     if el >= 4:
#         list0.append(el)
# print(list0)

list01 = list(filter(lambda x:x >=4, list1))
print(list01)
