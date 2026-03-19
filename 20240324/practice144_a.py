k=[]

fi = open("practice144_a.txt","r")
m = fi.read()
k = m.split(",")
fi.close()

sum = 0
for i in range(int(k[0]),int(k[1])+1,int(k[2])):
    sum+=i

print(sum)