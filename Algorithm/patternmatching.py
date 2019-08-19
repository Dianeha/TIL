def BruteForce(p, t):
    i = 0
    j = 0
    while j < len(p) and i < len(t):
        if t[i] != p[j]:
            i = i - j
            j = -1
        i = i + 1
        j = j + 1
    if j == len(p):
        return i - len(p)
    else:
        return -1

print(BruteForce("is", "This is a book~!"))

def Bmoore(pt, test):
    skip = [x for x in range(len(pt)+1)]







pt = 'rithm'
test = 'a pattern matching algorithm'
print(Bmoore(pt, test))