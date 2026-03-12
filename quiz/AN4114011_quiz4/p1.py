day = eval(input("請輸入天數:"))

def F(n):
    if(n==1): return 40
    else: return 2*F(n-1)+100

sum = 0
for i in range(1,day+1,1):
    sum+=F(i)

print("第",day,"天存入金額:",F(day))
print(day,"天共存入金額:",sum)