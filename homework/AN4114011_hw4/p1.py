x = input("請輸入密碼:")

if(x!="ncku"):
    for i in range(1,3,1):
        x = input("密碼錯誤,請再輸入一次密碼:")
        if(x=="ncku"):
            print("密碼正確")
            break
        if(i==2):
            print("已錯誤三次")
            break

else: print("密碼正確")