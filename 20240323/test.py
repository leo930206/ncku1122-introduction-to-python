sum_num = 0
sum_score = 0
i = 0
while(1):
    score = input("請輸入成績:")
    if(score==""): break
    sum_num+=1
    sum_score+=eval(score)

print("全班人數:",sum_num)
print("全班總分:",sum_score)