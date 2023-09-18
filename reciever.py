import os


os.chdir(r"D:\\projects\\python\\tmp\\recv")
list=sorted(os.listdir(),key=os.path.getmtime)
msg=""
for a in list:
    msg+=chr(int(a[-8:-6]))+chr(int(a[-6:-4]))+" "
    print(msg)   
    os.remove(a)
