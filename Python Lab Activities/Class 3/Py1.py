num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
num3 = int(input("Enter third number : "))

largest = 0

if num1 > num2:
	if num1 > num3:
		largest = num1
	else:
		largest = num3
else:
	if num2 > num3:
		largest = num2
	else:
		largest = num3

print(largest, "is the largest from given numbers")