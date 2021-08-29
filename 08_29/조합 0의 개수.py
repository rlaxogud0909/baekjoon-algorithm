# import sys

# def fac(n):
#     sum = 1
#     for i in range(1, n+1):
#         sum *= i
    
#     return sum

# a, b = map(int, sys.stdin.readline().split())
# cnt = 0

# result = list(str(int(fac(a) / (fac(b)*fac(a-b)))))
# print(result)

# for i in reversed(result):
#     if i == '0':
#         cnt += 1
#     else:
#         break

# print(cnt)

######################################################
# 시간 초과 발생
# 다른 해법

# 뒤에 0이 있는 경우는 10이 있는 경우를 의미한다.
# 즉 10은 2x5이니까 2의 개수와 5의 개수를 구하고 이 중 작은 값을 택하면 된다.
# 분자에 2가 4개 있고 분모에 2가 2개 있는 경우 -> 분자의 2의 개수에서 분모의 2의 개수를 빼면 된다.

import sys

# 2의 개수를 구하기
def two(n):
    sum = 0
    while n != 0:
        n = n//2
        sum += n
    return sum

def five(n):
    sum = 0
    while n != 0:
        n = n//5
        sum += n
    return sum

a, b = map(int, sys.stdin.readline().split())

# 분자의 개수에서 분모의 갯수 빼기 -> two(a)-two(b)-two(a-b)

# 이 중 가장 작은 값이 2와 5가 똑같은 값이다.
print(min(two(a)-two(b)-two(a-b), five(a)-five(b)-five(a-b)))

def twoCount(n):
    answer = 0
    while n != 0:
        n = n // 2 # 몫
        print(n)
        answer += n
    return answer

print(twoCount(25))

##############################################
#알아야할 것
# 1. 만약 10!에서 2로 나누어 떨어지는 갯수를 구하고 싶으면 10//2 -> 5개 + 5//2 -> 2개 + 2//2 -> 1개 이므로 총 8개
# 2. import math -> factorial

