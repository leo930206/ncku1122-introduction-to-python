print("請依序輸入兩整數m,n(m>n)")
m = eval(input("請輸入整數m:"))
n = eval(input("請輸入整數n:"))
F = M = 1

if(m<=n):
    print("m必須大於n，請重新輸入")
else:
    for i in range(2,m,1):
        if(m%i==0 and n%i==0):
            F=i
    
    for k in range(m,m*n,1):
        if(k%m==0 and k%n==0):
            M=k
            break
        elif(M==1):
            M=m*n

print("最大公因數是:",F)
print("最小公倍數是:",M)