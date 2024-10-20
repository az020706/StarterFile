avg=float(input("Please enter your average score:"))
if avg>=9:
    print("Congratulations! You've passed with high distinction!")
    print("Good luck to your academic path!")
elif avg>=7:
    print("You've passed with distinction!")
elif avg>=5:
    print("You've passed!")
else:
#Lệnh pass dùng để đánh dấu dòng cần code nhưng chưa sử dụng
    pass
    print("You've failed, study better next time!")