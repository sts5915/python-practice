# 파일 입출력
# 상대 경로( 내 위치 기준으로 가고 싶은곳으로)
#.은 현재 위치 c/test
#..은 바로 전 위치
#.현재위치 c/test/test1

# 절대 경로( 내 위치 상관없다)

# print("실행")
f = open("./test.txt", "w")
f.write("hello\n")
f.write("\n")
f.write("\n")
f.write("\tbye")
f.close()


# f = open("./test.txt", "r")
# lines = f.readlines()
# for line in lines :
#     print(line)
# f.close()

