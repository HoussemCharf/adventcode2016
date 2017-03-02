import math 

data = 3018458

binary = bin(data)[3:] + bin(data)[2]
print("Part one")
print(int(binary, 2))




largest = 1
current = 1
working = 1
for i in range(1, data + 1):
	current = i
	if working + 2 > current:
		largest = working
		working = 1
	elif working < largest:
		working += 1
	else:
		working += 2

print("Part two")
print(working)