import sys
sys.stdin = open("input.txt", "r")

def GNS(str):
    nums = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    nums_dict = {
        "ZRO": 0,
        "ONE": 0,
        "TWO": 0,
        "THR": 0,
        "FOR": 0,
        "FIV": 0,
        "SIX": 0,
        "SVN": 0,
        "EGT": 0,
        "NIN": 0,
    }

    for x in str.split():
        nums_dict[x] += 1

    result = []
    values = list(nums_dict.values())
    for i in range(len(nums)):
        for j in range(values[i]):
            result.append(nums[i])

    return ' '.join(result)

T = int(input())
for tc in range(1, T+1):
    info = input()
    str = input()
    print('#{}\n{}'.format(tc, GNS(str)))