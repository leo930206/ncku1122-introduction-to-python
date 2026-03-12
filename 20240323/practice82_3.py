n = eval(input("請輸入一個數字:"))

for i in range(1,n+1,1):
    for j in range(1,i+1,1):
        print("X",end="")
    print("")