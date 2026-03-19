n = eval(input("輸入一個正整數n:"))

for i in range(2,n+1,1):
    x = 0
    for j in range(1,i,1):
        if(i%j==0): x+=j
    if(i==x): print(i,end=" ")