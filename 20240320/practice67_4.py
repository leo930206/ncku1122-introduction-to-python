sum1 = sum2 = 0

for i in range(20,51,1):
    sum1 += i
    if(i%5==0):
        sum2 += i

print("20~50所有五的倍數之和: %d"%sum2)
print("20~50所有數的倍數之和: %d"%sum1)