with open("input.txt","r") as f:
  data = f.read().strip()

n = 0
ll = list()
la = list()

for l in data.split('\n'):
    ll.append(map(int, l.split()))

for i in range (len(ll)/3):
    for j in range(3):
        ln = [ll[i*3][j], ll[i*3+1][j], ll[i*3+2][j]]
        ln.sort()
        la.append(ln)

for l in la:
    if l[0]+l[1] > l[2]:
        n += 1

print n