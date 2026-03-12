S = 1
x = 0

for i in range(1,20,3):
    S *= (i+(2**x))
    x += 1

print(S)