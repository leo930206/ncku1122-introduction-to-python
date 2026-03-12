num = eval(input("請輸入一個數字: "))
sum = 0
 
if num > 1:
    for i in range(1,num,1):
        if(num%i==0):
            sum+=1
    if(sum==1):
        print(num,"是質數")
    else:
        print(num,"不是質數")

else:
   print(num,"不是質數")