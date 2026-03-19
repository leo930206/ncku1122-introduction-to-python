n = eval(input("請輸入n值:"))
m = eval(input("請輸入m值:"))

def F(x):
    if(x==1 or x==0): return 1
    else: return x*F(x-1)

result = F(n)/(F(m)*F(n-m))

print(result)