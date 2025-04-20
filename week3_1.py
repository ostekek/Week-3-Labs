number1 = input()
number2 = input()
number3 = input()

if number1 <= number2 :
    minimum = number1
else:
    minimum = number2
if number3 < minimum:
    minimum = number3
print(minimum)
