score_max = 0
score_min = 100
fail = 0

for i in range(1,11,1):
    print("請輸入第",i,"位同學成績:",end="")
    score = eval(input(""))
    
    if(score>score_max):score_max = score
    if(score<score_min):score_min = score
    if(score<60):fail+=1

print("最高分為:",score_max)
print("最低分為:",score_min)
print("不及格人數:",fail)