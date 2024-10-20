while True:
    n=int(input("Mời nhập một số nguyên dương:"))
    dem=0
    for i in range (1,n+1):
        if n % i ==0:
            dem+=1
    if dem==2:
        print(n, " là số nguyên tố")
    else:
        print(n, " không phải là số nguyên tố")
    hoi=input("Tiếp tục chương trình? (có/không)")
    if hoi == "không" or hoi == "Không":
        break
print("Cảm ơn bạn đã sử dụng")