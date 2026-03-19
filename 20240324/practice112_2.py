def F(n):
    if(n==1): return 10
    else: return 2*F(n-1)

x = eval(input("請輸入天數:"))

sum = 0
for i in range(1,x+1,1):
    sum=sum+F(i)

print("第",x,"天存了",F(x),"元")
print("第",x,"共天存了",sum,"元")