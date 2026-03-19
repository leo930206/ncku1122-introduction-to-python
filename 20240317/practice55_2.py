a = eval(input("請輸入a值:"))
b = eval(input("請輸入b值:"))
c = eval(input("請輸入c值:"))

if a>b and a>c:
    print(100)
elif c>b and c>a:
    print(10)
elif b>a and b>c:
    print(1)
else:
    print(0)