a=0
while a<100:
    b=0
    while b<40:
        if (a+b)%2==0:
            print("*",end='')
        b+=1
    print()
    a+=1
range(5)  #Starts from 0 to 4
range(5,10)  #Starts from 5 to 9
range(5,20,3)  #Starts from 5 to 19, increments by 3
range(20,5,-3)   #Starts from 20 to 6, decrements by 3
range(10,5)   #Starts from 10 to 6
range(0)  #No numbers included
range(10,101,10)  #Starts from 10 to 100, increments by 10
range(10,-1,-1)  #Starts from 10 to -1, decrements by 1
range(-3,4)  #Starts from -3 to 4
range(0,10,1)  #Starts from 0 to 9, increments by 1

for a in range(20,100,5):
    print("*", end='')
print()

n, m = 0, 100
while n != m:
    n = int(input())
    if n < 0:
        break
    print("n=",n)
