print("請依序輸入兩整數m,n(m>n)")
m = eval(input("請輸入整數m:"))
n = eval(input("請輸入整數n:"))
F = M = 1

if(m<=n):
    print("m必須大於n，請重新輸入")
else:5
    for k in range(1,m*n,1):
        if(m%k==0 and n%k==0):
            M=k

print("最小公倍數是:",M)