#제어문 복습
# a=5
# b=5
# if a > b:
#     print(f"{a}는 {b}보다 크다")
#     print("2")
#     print("3")
# elif a < b:
#     print(f"{a}는 {b}보다 작다")
# else : # 위 조건이 다 아니라면 다 아닐때 맨 마지막에 온다
#     print("else")


# x = {"company":"카카오"}
# if x.get("company")=="카카오" or x.get("company")=="네이버":
#      # and는 주어진 조건 전부 만족 즉 교집합 or는 이거나 저거나 둘중하나
#      # or을 쓰고 싶지 않다면 elif를 사용할 수 있다
#     print("대기업 직원이시네요")
# else:
#     print("중견기업 직원이시네요")

# match x.get("company"):   # and나 or을 쓸 수 없다
#     case "카카오":
#         print("대기업 이시네요")
#     case "네이버":
#         print("대기업 이시네요")
#     case _:
#         print("중견기업 이시네요")

# x = {"company":"카카오","isparttime":True}
# if x.get("company")=="카카오" or x.get("company")=="네이버":
#      # and는 주어진 조건 전부 만족 즉 교집합 or는 이거나 저거나 둘중하나
#      # or을 쓰고 싶지 않다면 elif를 사용할 수 있다
#     print("대기업 직원이시네요")
# else:
#     print("중견기업 직원이시네요")

# match x.get("company"):   # and나 or을 쓸 수 없다
#     case "카카오":
#         print("대기업 이시네요")
#     case "네이버":
#         print("대기업 이시네요")
#     case _:
#         print("중견기업 이시네요")



phone = {"name":"갤럭시", "version":"플립"}
# phone이 애플이면 와우
# 갤럭시면 
# verion을 보고 
# 플립이면 접히네요
# 아니면 좋네요

if phone.get("name")=="애플":
    print("와우")
elif phone.get("name")=="갤럭시":
    if phone.get("version")=="플립":
        print("접히네요")
    else :
        print("좋네요")

