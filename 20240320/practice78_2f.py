sum1=0

for i in range(1,4,1):
    sum2=0
    for j in range(3,2*i+4,2):
        sum2+=j
    sum1+=sum2

print(sum1)