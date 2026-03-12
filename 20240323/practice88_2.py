max = 0
fail = 0

for i in range(1,11,1):
    score = eval(input("請輸入第"+str(i)+"位同學成績:"))
    while(score<0 or score>100):
        score = eval(input("請重新輸入成績:"))
    
    if(score>max): max=score
    if(score<60): fail+=1

print("最高分為:",max)
print("不及格人數:",fail)