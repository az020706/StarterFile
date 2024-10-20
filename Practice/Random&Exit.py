#Random
import random
count=0
while True:
    x=random.randrange(-100,100)
    count+=1
    print(x,end='')
    if x==50:
        break
print("\nSố 50 thấy ở lần thứ:", count)
print("Bye!")

#Exit
while True:
    print("Nhập 1 số")
    n=int(input())
    dem=0
    for i in range(1,n+1):
        if n % i ==0:
            dem+=1
    if (dem==2):
        print(n,"là số nguyên tố!")
    else:
        print(n,"không là số nguyên tố")
    k=input("Continue?(y/n):")
    if k=="n":
        exit()
    #Any line under the exit command will be skipped and ended directly
    print("Bye!")

#Eval
from math import *
s="(5*6)-(7/2)+8+sin(0.5)+pow(2,3)"
x=eval(s)
print(x)

x1,x2=eval(input("Enter x1,x2"))
print("x1=",x1,"x2=",x2)
