n = eval(input("請輸入n值:"))

def F(x):
    if(x==1 or x==0): return 1
    else: return x*F(x-1)

result = 0
for i in range(0,n+1,1):
    result += F(n)/(F(i)*F(n-i))

print(result)