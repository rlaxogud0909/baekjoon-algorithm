# 출현 횟수
#1은 3번
#2는 2번
#3은 1번
#4는 1번

# counterㅎ사용
import sys
from collections import Counter

n = sys.stdin.readline()
a = list(sys.stdin.readline().split())


b = Counter(a)

c = [ [i, b[i]] for i in a ]

# print(c)

result = [-1] * len(a)
stack = []
stack.append(0)
i = 1

while stack and i<len(a):
    while stack and c[stack[-1]][1]<c[i][1]:
        result[stack.pop()]=c[i][0]

    stack.append(i)
    i+=1

print(*result)