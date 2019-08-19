s = 'Reverse this string'
s1 = s[::-1]

s2 = [x for x in s]
s2.reverse()
s2 = ''.join(s2)

a = [x for x in s]
for i in range(len(a)//2):
    a[i], a[-1-i] = a[-1-i], a[i]
s3 = ''.join(a)

print(s1)
print(s2)
print(s3)