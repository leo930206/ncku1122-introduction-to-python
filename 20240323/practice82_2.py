num_90 = 0
max_c = 0
min_m = 100
fail_e = 0
sum_c = sum_e = sum_m = 0

for i in range(1,11,1):
    
    score_c = eval(input("請輸入第"+str(i)+"位同學國文成績:"))
    score_e = eval(input("請輸入第"+str(i)+"位同學英文成績:"))
    score_m = eval(input("請輸入第"+str(i)+"位同學數學成績:"))

    if(score_c>90 and score_e>90 and score_m>90): num_90+=1
    if(score_c>max_c): max_c=score_c
    if(score_m<min_m): min_m=score_m
    if(score_e<60): fail_e+=1

    sum_c += score_c
    sum_e += score_e
    sum_m += score_m

ave_c = score_c/10
ave_e = score_e/10
ave_m = score_m/10

print("三科成績皆90分以上人數:",num_90)
print("全班國文最高分:",max_c)
print("全班數學最低分:",min_m)
print("全班英文不及格人數:",fail_e)
print("全班國文的平均分數:",ave_c)
print("全班英文的平均分數:",ave_e)
print("全班數學的平均分數:",ave_m)