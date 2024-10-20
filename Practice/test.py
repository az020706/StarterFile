def convert_to_words(n):
    # Two arrays for one-digit and two-digit numbers
    one = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    ten = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']

    if n == 0:
        return 'Zero'

    if n > 9 and n < 20:
        # for numbers 10 to 19
        words = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        return words[n - 10]
    else:
        # for two digit numbers
        return ten[n//10] + ' ' + one[n%10]

# Input a 2-digit number
num = int(input("Enter a 2-digit number: "))

if num < 10 or num > 99:
    print("Please enter a valid 2-digit number.")
else:
    words = convert_to_words(num)
    print(words)