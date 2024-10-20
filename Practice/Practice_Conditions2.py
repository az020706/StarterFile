def convert_to_words(n):
   one = ['', 'mốt', 'hai', 'ba', 'bốn', 'năm', 'sáu', 'bảy', 'tám', 'chín']
   ten = ['', 'mười', 'hai', 'ba', 'bốn', 'lăm', 'sáu', 'bảy', 'tám', 'chín']

   if n==0:
       return 'Zero'

   if n>=10 and n<20:
       return ten[n//10] + ' ' + one[n%10]

   else:
       return ten[n//10] + ' mươi ' + one[n%10]

num = int(input("Enter a 2-digit number: "))
if num < 10 or num > 99:
    print("Please enter a valid 2-digit number.")
else:
    words = convert_to_words(num)
    print(words)
