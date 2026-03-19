e = eval(input("請輸入用電度數:"))

while(e<1 or e>950):
    e = eval(input("請重新輸入用電度數:"))

if(e<100): sum=e*2.2
elif(e<=300): sum=(100*2.2)+((e-100)*3.3)
elif(e>300): sum=(100*2.2)+(200*3.3)+((e-300)*4.4)

print("應繳交電費:",sum,"元",sep="")