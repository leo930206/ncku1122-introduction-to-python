max = 0
min = 100
up_0 = under_0 = 0

for i in range(1,11,1):
    print("請輸入第",i,"個數:",end="")
    num = eval(input(""))

    if(num>max): max=num
    if(num<min): min=num
    if(num<0): under_0+=1
    if(num>0): up_0+=1

print("最高為:",max)
print("最低為:",min)
print("大於0有:",up_0,"個")
print("小於0有:",under_0,"個")