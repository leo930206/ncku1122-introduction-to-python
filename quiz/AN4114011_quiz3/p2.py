n = int(input("輸入正整數n: "))

for i in range(1,n+1,1):
    print(" "*(n-i),end="")
    for j in range(0,i,1):
        print("* ",end="")
    print()