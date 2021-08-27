ss = list(input())
result = [0] * 26

for s in ss:
    idx = ord(s)-ord('a')
    result[idx] += 1

for i in result:
    print(i, end=' ')