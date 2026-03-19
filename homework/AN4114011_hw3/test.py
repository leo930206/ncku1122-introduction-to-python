n = eval(input("輸入一個正整數n:"))

for i in range(2,n+1,1):
    x = 0
    print("      現在是i=",i)
    for j in range(1,i,1):
        print("   現在是j=",j)
        if(i%j==0): 
            x+=j
            print("現在是x=",x)
        if(i==j): print(i,end=" ")