'''n=4
for i in range(n):
    for j in range(n):
        if i==n-1 or i==0 or j==0 or j==n-1:
            print("* ",end='')
        else:
            print("  ",end='')
    print()'''

n=int(input("Please enter number"))
for i in range(n, 0, -1):
    for j in range(0, n):
        if j >= i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

'''n=4
for i in range(n):
    for j in range(i+1):
        print("*", end='')
    print()'''