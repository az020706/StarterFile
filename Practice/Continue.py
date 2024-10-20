n=int(input("Please enter a number:"))
s=0
for x in range(1,n+1,2):
    if x == 3 or x == 11:
        continue
    s+=x
print("Your total=", s)