a=eval(input("請輸入第一次TOEIC成績:"))
b=eval(input("請輸入第二次TOEIC成績:"))
c=eval(input("請輸入第三次TOEIC成績:"))

sum = a+b+c
average = sum/3

print("三次平均分數為:",average,"第一次考試與平均差幾分:",a-average)