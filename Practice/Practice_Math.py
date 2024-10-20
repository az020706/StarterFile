#Tính chu vi hình tròn
import math

try:
    radius = float(input('Please enter radius number:'))
    P = 2*math.pi*radius
    A = pow(radius,2)*math.pi
    print("The perimeter of the circle is:", P)
    print("The area of the circle is:", A)
except:
    print("Invalid number, please try again!")

#Tính giờ, phút theo giây
try:
    t = float(input('Please insert an amount of seconds:'))
    h = (t//3600)%24
    m = (t%3600)//60
    s = (t%3600)%60
    print('Your time is:', h, ':', m, ':', s)
except:
    print('Invalid, please try again!')

#Tính điểm trung bình
math=float(input('Please enter your math score:'))
physic=float(input('Please enter your physic score:'))
chemistry=float(input('Please enter your chemistry score:'))
avg=(math+physic+chemistry)/3
print("Your average score is:",round(avg,2))