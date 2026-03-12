C = []
E = []
max_c = max_e = 0

for i in range(6):
    score=eval(input("第"+str(i+1)+"位同學國文成績:"))
    C.append(score)
    score=eval(input("第"+str(i+1)+"位同學英文成績:"))
    E.append(score)

    if(C[i]>max_c): max_c=C[i]
    if(E[i]>max_e): max_e=E[i]

print("國文最高分:",max_c)
print("英文最高分:",max_e)