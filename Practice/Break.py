# Ví dụ
# while True:
    # a=int(input("Nhập giá trị:"))
    # print("Giá trị bạn nhập =", a)
    # s=input("Tiếp tục phần mềm không (c/k):")
    # if s =="c":
        # break
# print("Bye!")
while True:
    x=int(input("Nhập vào số:"))
    print(x,"là số chẵn" if x % 2==0 else "là số lẻ")
    s=input("Tiếp tục không (y/n)")
    if s=="n":
        break
print("bye!")

n=int(input("Nhập N:"))
s=0
for x in range(1,n+1):
    s+=x
    if s > 15:
        break
print("S=", s)