n = eval(input("請輸入一個三位數(100~999):"))
num = n

a = num//100
num -= a*100
b = num//10
num -= b*10
c = num

sum = (a**3)+(b**3)+(c**3)

if n>=100 and n<=999:
    if(sum == n):
        print(n,"是阿姆斯壯數")
    else:
        print(n,"不是阿姆斯壯數")
else:
    print("數字不在範圍內")