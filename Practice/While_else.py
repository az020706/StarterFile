count=sum=0
print("Nhập 5 số lớn hơn hoặc bằng 0 để tính trung bình:")
#vòng lặp while phải dừng khi có 5 giá trị
while count<5:
    val=int(input("Nhập giá trị:"))
    if val<0:
        print("Nhập sai quy tắc")
        break
    sum=sum+val
    count=count+1
else:
    print("Trung bình=", sum/count)