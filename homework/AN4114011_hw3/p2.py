n = eval(input("輸入一個整數n:"))

for i in range(0,n,1):
    for j in range(0,n,1):
        if(i==j or i+j==n-1):
            print("*",end="")
        else:
            print(" ",end="")
    print()