#For loop
n=int(input("Nhập chiều cao:"))
#Vertical line
for i in range(n):
    #Horizontal line
    for j in range(n):
        if j==0 or i==j or j==n-1:
            print("*",end='')
        else:
            print(' ', end='')
    print()
#While loop
print("#"*30)
i=0
while i<n:
    j=0
    while j<n:
        if j==0 or i==j or j==n-1:
            print("#",end='')
        else:
            print(" ",end='')
        j+=1
    i+=1
    print()
