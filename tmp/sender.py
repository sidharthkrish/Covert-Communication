import os 
import random
import time


def sender():
        m="HEL"
        m.upper()
        if len(m)//2==0:
             pass
        else:
            m+="Z"
        items=["user","ssh","mongodb","dwnld"]
        for x in range(0,len(m),2):
            pair=m[x:x+2]
            random.shuffle(items)
            filename=items[0]+str(ord(pair[0]))+str(ord(pair[1]))+".txt"
            filename=folder_name+"\\"+filename
            print(filename)
            with open(filename,"w") as f:
                text = ''.join(random.choice('10') for _ in range(random.randint(50,500))) #write random number of 1 or 0.
                f.write(text)
                f.close()
                time.sleep(random.randint(1,5))


folder_name="D:\\projects\\python\\tmp\\recv" # change to temp folder.
if os.path.exists(folder_name):
    os.chdir(folder_name)
    x=os.listdir()
    if len(x)==0:
        sender()
    else:
         pass
        


