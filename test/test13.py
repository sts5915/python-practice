# 상대 경로, 절대 경로 복습
# 업데이트와 class

# f = open("./test.txt", "w")
# f.write("""hi


#     bye""")
# f.close()

#def open(filename, type):
    #filename이 있냐
    #if type =='w':
        #쓰기모드
    #if type =='r':
        #읽기모드
# fr  = open("./88888888.txt", "r", encoding="UTF-8")
# lines = fr.readlines()
# #lines = ["빅데이터","파이썬","AI"]
# for line in lines:
#     print(line)
# fr.close()

# fw = open("./88888888.txt", "w", encoding="UTF-8")
# for line in lines:
#     if line == "한글":   # 실제로는 뒤에 엔터를 친 경우라 적용이 안되었던 것이다
#         fw.write("ai")
#     elif line == "읽기":
#         fw.write("GIT")
#     else:
#         fw.write(line)
# fw.close()


# 첫번째줄 빼고 다 바꿔보기

#8 바꿀문장, 취소는 c 9999  ML 바꿀문장, 취소는 c hihihi 글쓰기 바꿀문장, 취소는c c 읽기 바꿀문장, 취소는 cc
fr = open("./12345.txt", "r", encoding="UTF-8")
lines = fr.readlines()
fr.close()


fw = open("./12345.txt", "w", encoding="UTF-8")
for line in lines:
    update_text = input(f"전 문장 : {line}\n 바꿀 문장(취소는 c) : \t")
    if update_text == "c":
        fw.write(line.strip())
    else:
        fw.write(update_text)
    fw.write("\n")
fw.close()










