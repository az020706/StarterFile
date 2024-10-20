x=int(input("Mời bạn nhập số năm"))
print("Năm nhuận!" if x % 4 == 0 and x % 100 != 0 or x % 400 ==0 else "Năm không nhuận")

y=int(input("Mời bạn nhập tháng"))
if y in (1,3,5,7,8,10,12):
    print("Tháng", y, "có 31 ngày")
elif y in (4,6,9,11):
    print("Tháng", y, "có 30 ngày")
elif y ==2:
    year=int(input("Mời bạn nhập số năm"))
    if (year % 4 ==0 and year % 100 !=0) or year % 400 ==0:
        print("Tháng", y, "có 29 ngày")
    else:
        print("Tháng", y, "có 28 ngày")
else:
    print("Tháng", y, "không hợp lệ!")