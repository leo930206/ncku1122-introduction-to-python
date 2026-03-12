x = int(input("輸入正整數x:"))

sum = 0

for i in range(1,x+1,1):
    s = 0
    for j in range(1,i+1,1):
        s+=j
    sum+=s

print(sum)