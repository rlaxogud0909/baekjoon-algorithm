n = list(input())

stack = [-1] * 26
j = 0
for i in n:
    idx = ord(i) - ord('a')
    if stack[idx] == -1:
        stack[idx] = j
    j+=1

for s in stack:
    print(s, end=' ')

