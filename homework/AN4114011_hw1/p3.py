a=eval(input("請輸入a邊長:"))
b=eval(input("請輸入b邊長:"))
c=eval(input("請輸入c邊長:"))

s=(a+b+c)/2

area=(s*(s-a)*(s-b)*(s-c))**0.5

print(area)