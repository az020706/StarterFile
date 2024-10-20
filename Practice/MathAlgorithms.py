from math import *

x=5
y=7
print(pow(x,y))
print(x**y)
print(sqrt(25))
do=30
print('30 do =>', radians(do))
rad=radians(do)
print(degrees(rad))
print("log10(100) =", log10(100))

#Sin,cos,tan
'''print("Mời bạn nhập một góc:")
goc=float(input())
sinx=sin(radians(goc))
cosx=cos(radians(goc))
tanx=tan(radians(goc))
cotx=1/tanx
print("sin({0})={1}".format(goc,sinx))
print("cos({0})={1}".format(goc,cosx))
print("tan({0})={1}".format(goc,tanx))
print("cot({0})={1}".format(goc,cotx))'''

#Round(original number,count of decimal rounded)
'''x=5
y=7
z=x/y
print("z=",round(z,2))
print("z=",round(z,5))
k=round(z,5)
print("k=",k)
print("z=",z)'''

#Time, clock and sleep

import time
print("Enter your name:", end='')
start_time = time.perf_counter()
name = input()
elasped = time.perf_counter()-start_time
print(name,"it took you",elasped,"seconds to respond")

import time
for count in range(10,-1,-1): #Range 10,9,...,1,0
    print(count) #Display count
    time.sleep(1) #Suspend execution for 1 second
