sum = 0

for i in range(1,101,1):
    if(i>=21 and i <=50):
        if(i%2==1):
            sum += i
            print(i)

print("總和為: %d"%sum)