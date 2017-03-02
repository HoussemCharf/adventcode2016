import itertools
import hashlib

salt = 'reyedfim'
ans1, ans2 = [], {}
for n in itertools.count():
    seed = '{}{}'.format(salt, n).encode()
    digest = hashlib.md5(seed).hexdigest()
    if digest.startswith('00000'):
        x, y = digest[5:7]
        if len(ans1) < 8: ans1.append(x)
        if x in '01234567' and x not in ans2: ans2[x] = y
        if len(ans1) == 8 and len(ans2) == 8: break

print(''.join(ans1))
print(''.join(v for k,v in sorted(ans2.items())))