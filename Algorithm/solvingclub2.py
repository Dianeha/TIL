import sys
sys.stdin = open("input.txt", "r")

nums = ["ZRO", 0, "ONE", 1, "TWO", 2, "THR", 3, "FOR", 4, "FIV", 5, "SIX", 6, "SVN", 7, "EGT", 8, "NIN", 9, ]


def GNS(data, str):
    s = str.split()
    numbers = [nums[nums.index(x) + 1] for x in s]
    cnt = [0] * data

    for



    return ' '.join([nums[nums.index(number) - 1] for number in numbers])


T = int(input())
for tc in range(1, T + 1):
    data = input().split()[1]
    str = input()
    print('#{}\n{}'.format(tc, GNS(data, str)))
