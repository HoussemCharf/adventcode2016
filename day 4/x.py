def occ(x):
	l=list()
	l2=list()
	code=""
	code= x.split("[",1)[1].split("]",1)[0]
	for i in range (0,len(code)):
		l.append(x.split("[",1)[0].count(code[i]))
	l2=sorted(l,reverse=True)
	return l==l2

with open("input.txt","r") as f:
  data = f.read().strip()
result=0

for line in data.split("\n"):
	if occ(line) :
		result+=int(filter(str.isdigit,line))
print result