money = eval(input("請輸入今日賣豆花賺的錢:"))

if money>999:
    print("金額大於999，錯誤")
else:
    a = money//100
    b = (money-(a*100))//10
    c = money-((a*100)+(b*10))
    print(a,"個百元")
    print(b,"個十元")
    print(c,"個壹元")