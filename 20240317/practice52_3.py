temp = eval(input("請輸入今日溫度:"))
AQI = eval(input("請輸入今日空氣品質:"))

if temp>37 or AQI>150:
    print("避免外出")
else:
    print("可依需要待在戶外")