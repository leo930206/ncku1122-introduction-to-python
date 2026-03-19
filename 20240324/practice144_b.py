k=[]

fi= open("practice144_b.txt", "r")
for i in range(0,3,1):
    k.append(eval(fi.readline()))
fi.close()

sum = 0
for i in range(k[0],k[1]+1,k[2]):
    sum+=i

print(sum)