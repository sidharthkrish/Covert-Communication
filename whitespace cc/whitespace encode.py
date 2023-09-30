msg="hello"
list=[]
bmsg=""
for x in msg:
    a=bin(ord(x))
    for b in a[2:]:
        if b=="1":
            bmsg+="a\t"
        if b=="0":
            bmsg+="b "
    list.append(bmsg)
    bmsg=""

with open("cc.txt","w") as f:
    for a in list:
        f.write(a+"\n")
f.close()
