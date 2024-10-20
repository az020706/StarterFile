#Bình phương 1 số từ 1 đến 10
print("Nhập 1 số [1,...10]: ")
x=-1
while x<1 or x>10:
    x=int(input("Nhập 1 số [1,...10]: "))
print(x**2)
#s=1+2+3+...+N
print("Nhập N: ")
n=int(input(""))
s=0
i=1
while i<=n:
    s=s+i
    i=i+1
print("Tổng= ", s)