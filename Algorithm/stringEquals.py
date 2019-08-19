import sys
sys.stdin = open("input2.txt", "r")

def BruteForce(pattern, test):
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
    pattern = input()
    test = input()
    print('#{} {}'.format(tc, BruteForce(pattern, test)))