age = int(input("Enter you age : "))

if age < 18:
	print("You are not yet old enough to vote.")
elif 18<=age <65:
	print("You are old enough to vode.")
elif 65<=age<100:
	print("You are eligible for seniors dirsount")
elif age>= 100:
	print("You are a centurian.")