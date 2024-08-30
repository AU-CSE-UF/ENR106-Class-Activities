list1 = [1, "Hello", "World", 3]
list2 = [1, "Hello", "World", 3]

count = 0

for i in list1:
	for j in list2:
		if i is j:
			count+=1

if len(list1) == len(list2) and len(list1) == count:
	print("Both the lists are same")
else:
	print("Both the lists are different")