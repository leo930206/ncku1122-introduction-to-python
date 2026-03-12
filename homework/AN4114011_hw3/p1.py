n = eval(input("輸入一個正偶數n:"))

if(n%2!=0): 
    print("請輸入正偶數")
    exit()

sum1 = 1

for i in range(1,(n//2)+1,1):
    sum2 = 0
    for j in range(2,(i*2)+1,2):
        sum2 += j
    sum1 *= sum2

print(sum1)

sum1=0