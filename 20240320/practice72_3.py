sum1 = sum2 = 0       #sum1為1~30 sum2為10~60

for i in range(1,6,1):
    print("請輸入第",i,"個數:",end="")
    num = eval(input(""))

    if(num>=1 and num<=30): sum1+=1
    if(num>=10 and num<=60): sum2+=1

print("值介於1~30之間有:",sum1,"個")
print("值介於10~60之間有:",sum2,"個")