S = 0
x = 0

for i in range(1,12,2):
    a = i*(3**x)
    x += 1
    if(x%2==0):
        a = -a
    S += a

print(S)