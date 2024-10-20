#Phân biệt số ảo dạng a + bi
z=complex(2,3)
print ("Phần thực =",z.real)
print ("Phần ảo =",z.imag)
x=complex(4,5)
print("Phần thực =",x.real,"; Phần ảo =",x.imag)
year=2018
t=year % 2 ==0 and year % 3 > 1
print(t)
t=year % 2 ==0 and year % 3 > 5
print(t)
#Nhập liệu
s=float(input("Mời bạn nhập giá trị:"))
print("Bạn nhập =",s)
print(type(s))
def StrToBool(s):
    return s.lower() in ("true", "t", "1", "yes")
x=input("Mời bạn nhập True hay False:")
x=StrToBool(x)
print(x)
print('Please enter 2 numbers to divide')
dividend = float(input('Please enter dividend number:'))
divisor = float(input('Please enter divisor number:'))
#Thực hiện phép chia
result = dividend / divisor
#Phép chia 2 số
print(dividend, '/', divisor, "=", result)