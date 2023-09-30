hidden=""
list=[]
# filename=input("include extn")
with open("test.txt", "r") as file:
    x= file.read().split("\n")
    for line in x:
        print(line)
        for char in line:
            counter=len(line)
            index=line.find(char)
            if char==" ":
                hidden+="0"
                
            if char=="\t":
                hidden+="1"
        list.append(hidden[-7:]) 
 
        hidden="" 
print(list)     


msg = ""

for element in list:
    try:
        msg += chr(int(element, 2))
    except:
        pass
    
print(msg)
        
