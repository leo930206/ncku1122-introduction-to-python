def F(n):
    if(n==1): return 1
    else: return (2*F(n-1))+3

k = eval(input("請輸入一個數字:"))

print(F(k))