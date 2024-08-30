sub1 = float(input("Enter marks of first subject(out of 100) : "))
sub2 = float(input("Enter marks of second subject(out of 100) : "))
sub3 = float(input("Enter marks of third subject(out of 100) : "))

percentage = (sub1 + sub2 + sub3) / 3

if percentage >= 70:
	print("Passed with distinct class.")
elif 70 > percentage >= 60:
	print("Passed with first class.")
elif 60 > percentage >= 50:
	print("Passed with second class.")
elif 50 > percentage >= 40:
	print("Just passed.")
else:
	print("Failed.")