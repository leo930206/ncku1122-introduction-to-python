s = []
fail_e = 0
max_c = max_e = 0

for i in range(5):
    k = []
    score=eval(input("第"+str(i+1)+"位同學國文成績:"))
    k.append(score)
    score=eval(input("第"+str(i+1)+"位同學英文成績:"))
    k.append(score)
    s.append(k)

    if(s[i][1]<60): fail_e+=1

print("英文不及格人數:",fail_e)