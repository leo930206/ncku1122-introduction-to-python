def add(a,b): return a+b
def sub(a,b): return a-b
def mul(a,b): return a*b
def div(a,b): return a/b

import random

while(1):
    x=random.randint(1,100)
    y=random.randint(1,100)

    z=random.randint(1,4)
    if(z==1): m=add(x,y);i="+"
    elif(z==2): m=sub(x,y);i="-"
    elif(z==3): m=mul(x,y);i="*"
    elif(z==4): m=div(x,y);i="/"

    print(x,i,y,"=?",sep="")
    ans = eval(input("輸入答案:(如果要結束請輸入9999)"))

    if(ans==9999): break

    if(ans==m): print("答對了!")
    else: print("答錯了><")