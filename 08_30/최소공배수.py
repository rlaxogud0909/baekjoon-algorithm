# 풀이 1) 시간초과
# n = int(input())

# for _ in range(n):
#     number1, number2 = map(int, input().split())

#     data1 = []
#     data2 = []

#     for i in range(1, number2+1): # 첫번째 배수를 구함
#         data1.append(i*number1)
#     for i in range(1, number1+1): # 두번째 배수를 구함
#         data2.append(i*number2)

#     for i in data1: # 첫번째 배수와 두번째 배수가 같은 것 중 가장 작은 값 추출
#         if i in data2: 
#             lcm = i
#             break
#     print(lcm)


# 풀이2) 시간 초과
# def calculate(num1, num2):
#     i = 1
#     sum = 1
#     while (i != num1+1):
#         if num1 % i == 0 and num2 % i == 0:
#             # print('i:', i)
#             num1 //= i
#             num2 //= i 
#             sum *= i
#             i=1
#         i+=1
#     return sum * num1 * num2

# n = int(input())

# for _ in range(n):
#     num1, num2 = map(int, input().split())
#     print(calculate(num1, num2))

# 풀이 3) 시간초과
# import sys

# n = int(sys.stdin.readline())


# for _ in range(n):
#     num1, num2 = map(int, sys.stdin.readline().split())
#     for i in range(1, num1+1):
#         if num1 % i == 0 and num2 % i == 0:
#             gcd = i
#     print((num1//gcd)*(num2//gcd)*gcd)


n = int(input())

for i in range(n): 
    a,b=map(int, input().split())
    A, B=a,b 
    while B != 0: 
        A=A%B 
        A,B=B,A 
        
    print(a*b//A)

# 6 10 진행 과정
# 6 % 10 -> 6      10  6
# 10 % 6 -> 4      6   4
# 6 % 4  -> 2      4   2
# 4 % 2  -> 0      2   0  -> A가 최대 공약수