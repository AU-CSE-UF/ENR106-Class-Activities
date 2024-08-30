itr = int(input("Enter number of iterations(greater than or equal to 3) : "))

fnum = 0
snum = 1
nnum = 0

print(fnum)
print(snum)
nnum = fnum + snum
print(nnum)
i = 3
for i in range(3, itr):
	fnum = snum
	snum = nnum
	nnum = fnum + snum
	print(nnum)