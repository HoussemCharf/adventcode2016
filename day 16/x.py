data = "11101000110010100"



def fill(a, length):
    while len(a) < length:
        b = a[::-1]
        b = b.replace("1", "2").replace("0", "1").replace("2", "0")
        a = a + "0" + b 
    return a[:length]

def checksum(a):
    c = []
    for two in zip(a[0::2], a[1::2]):
        if two[0] == two[1]:
            c += "1"
        else:
            c += "0" 
    c = "".join(c)
    while len(c) % 2 == 0:
        c = checksum(c)
    return c 

print("PART 1:")
print(checksum(fill(data, 272)))

print("PART 2:")
print(checksum(fill(data, 35651584)))