import sys
sys.stdin = open("input4865.txt", "r")

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    str1_list = []
    for x in str1:
        if x not in str1_list:
            str1_list.append(x)

    res = {}
    for x in str2:
        if x in str1_list:
            if x in res:
                res[x] += 1
            else:
                res[x] = 1

    s = list(res.values())
    max = s[0]
    for i in s:
        if i > max:
            max = i

    print("#{} {}".format(tc, max))