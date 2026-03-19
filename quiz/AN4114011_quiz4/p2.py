n = eval(input("請輸入n值(n>3):"))

def F(n):
    if(n==1 or n==2 or n==3): return 1
    else: return F(n-1)+F(n-2)+F(n-3)

sum = 0
for i in range(1,n+1,1):
    print(F(i),end=" ")
    sum+=F(i)

print("")
print("總合為:",sum)