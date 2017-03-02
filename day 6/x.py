import collections

with open("input.txt","r") as f:
  data = f.read().strip()
listofclums = []
a_list = []
listofwords = []
most_word=''
least_word=''
for i in range (0,8):
	del a_list[:]
	for line in data.split("\n"):
		a_list.append(line[i])
	listofclums.append(a_list)
	listofwords.append(''.join(listofclums[i]))

for elem in listofwords:
	most_word+=collections.Counter(elem).most_common(1)[0][0]
	least_word+=collections.Counter(elem).most_common()[-1][0]

print most_word
print least_word

