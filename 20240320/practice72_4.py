num = eval(input("請問班上有幾位同學:"))

score_max = 0
score_900 = 0
score_600_700 = 0
score_sum = 0

for i in range(1,num+1,1):
    print("請輸入第",i,"位同學TOEIC成績:",end="")
    score = eval(input(""))
    
    score_sum+=score
    if(score>score_max):score_max = score
    if(score>900):score_900 += 1
    if(score>=600 and score<=700): score_600_700 += 1

ave = score_sum/num

print("TOEIC 全班最高分為:",score_max)
print("TOEIC 900分以上人數:",score_900)
print("TOEIC 600到700分人數:",score_600_700)
print("TOEIC 全班總平均分數:",ave)