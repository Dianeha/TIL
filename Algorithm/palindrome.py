import sys
sys.stdin = open("palindrome.txt", "r")

def Palindrome(pattern, test):
    i = 0
    j = 0
    while i < len(pattern) and j < len(test):
        if pattern[i] != test[j]:
            j = j - i
            i = - 1
        i += 1
        j += 1
    if i == len(pattern):
        return 1
    else:
        return 0

T = int(input())
for tc in range(1, T+1):
    rc= input().split()
    r = rc[0]
    c = rc[1]

    print('#{} {}'.format(tc, Palindrome(pattern, test)))