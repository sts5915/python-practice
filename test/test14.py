fr = open("./1122.txt","r",encoding="UTF-8")
lines=fr.readlines()
fr.close()

fw = open("./1122.txt","w", encoding="UTF-8")
print(lines)
for line in lines :
    update_text = input(f"전 문장 : {line}\n 바꿀 문장(취소는 c) : \t")
    if update_text == "c":
        fw.write(line)
    else :
        fw.write(update_text)
    
fw.close()