x = int(input("輸入正整數x:"))

n_1 = n_2 = 1

for i in range(2,x+1,1):
    n = n_1+n_2
    n_1 = n_2
    n_2 = n

print(n)