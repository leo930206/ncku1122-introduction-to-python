position1=position2=position3=position4=position5=position6=position7=position8=position9=" "
num = 0

while(num<10):
    if(position1==position2==position3=="o"): print("玩家1獲勝!");break
    elif(position4==position5==position6=="o"): print("玩家1獲勝!");break
    elif(position7==position8==position9=="o"): print("玩家1獲勝!");break
    elif(position1==position4==position7=="o"): print("玩家1獲勝!");break
    elif(position2==position5==position8=="o"): print("玩家1獲勝!");break
    elif(position3==position6==position9=="o"): print("玩家1獲勝!");break
    elif(position1==position5==position9=="o"): print("玩家1獲勝!");break
    elif(position3==position5==position7=="o"): print("玩家1獲勝!");break
    elif(position1==position2==position3=="x"): print("玩家2獲勝!");break
    elif(position4==position5==position6=="x"): print("玩家2獲勝!");break
    elif(position7==position8==position9=="x"): print("玩家2獲勝!");break
    elif(position1==position4==position7=="x"): print("玩家2獲勝!");break
    elif(position2==position5==position8=="x"): print("玩家2獲勝!");break
    elif(position3==position6==position9=="x"): print("玩家2獲勝!");break
    elif(position1==position5==position9=="x"): print("玩家2獲勝!");break
    elif(position3==position5==position7=="x"): print("玩家2獲勝!");break
    elif(position1==" " or position2==" " or position3==" " or position4==" " or position5==" " or position6==" " or position7==" " or position8==" " or position9==" "): pass
    else: print("平手!");break

    if(num==0 or num==2 or num==4 or num==6 or num==8):
        player1 = eval(input("玩家1請選擇位置:"))
        while(player1<1 or player1>9 or (position1!=" " and player1==1)or(position2!=" " and player1==2)or(position3!=" " and player1==3)or(position4!=" " and player1==4)or(position5!=" " and player1==5)or(position6!=" " and player1==6)or(position7!=" " and player1==7)or(position8!=" " and player1==8)or(position9!=" " and player1==9)): 
            player1 = eval(input("位置錯誤，玩家1請重新選擇位置:"))

        if(player1==1): position1="o"
        elif(player1==2): position2="o"
        elif(player1==3): position3="o"
        elif(player1==4): position4="o"
        elif(player1==5): position5="o"
        elif(player1==6): position6="o"
        elif(player1==7): position7="o"
        elif(player1==8): position8="o"
        elif(player1==9): position9="o"

        num+=1
        print(position1,position2,position3,sep="")
        print(position4,position5,position6,sep="")
        print(position7,position8,position9,sep="")
        continue

    if(num==1 or num==3 or num==5 or num==7):
        player2 = eval(input("玩家2請選擇位置:"))
        while(player2<1 or player2>9 or (position1!=" " and player2==1)or(position2!=" " and player2==2)or(position3!=" " and player2==3)or(position4!=" " and player2==4)or(position5!=" " and player2==5)or(position6!=" " and player2==6)or(position7!=" " and player2==7)or(position8!=" " and player2==8)or(position9!=" " and player2==9)): 
            player2 = eval(input("位置錯誤，玩家2請重新選擇位置:"))

        if(player2==1): position1="x"
        elif(player2==2): position2="x"
        elif(player2==3): position3="x"
        elif(player2==4): position4="x"
        elif(player2==5): position5="x"
        elif(player2==6): position6="x"
        elif(player2==7): position7="x"
        elif(player2==8): position8="x"
        elif(player2==9): position9="x"

        num+=1
        print(position1,position2,position3,sep="")
        print(position4,position5,position6,sep="")
        print(position7,position8,position9,sep="")
        continue