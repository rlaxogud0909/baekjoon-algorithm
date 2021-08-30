# 24 18

# sum = 1
# first = 24
# second = 18

# 최대 공약수 (내풀이)
# i = 1
# while (i != first+1):
#     if first % i == 0 and second % i == 0:
#         # print('i:', i)
#         first //= i
#         second //= i 
#         sum *= i
#         i=1
#     i+=1

# print(sum)

# first_1 = 36
# second_1 = 48

#최대 공약수 (즉 최대로 같이 나누어떨어지는 수가 최대 공약수)
# 여기서 +) gcd가 1이면 두 값은 서로소이다.
# for i in range(1, first_1+1):
#     if first_1 % i == 0 and second_1 % i == 0:
#         gcd = i

# print(gcd) 

# 최소 공배수 (내풀이 최대공약수에서 서로소 나머지 값을 곱해줌)
# i = 1
# while (i != first+1):
#     if first % i == 0 and second % i == 0:
#         # print('i:', i)
#         first //= i
#         second //= i 
#         sum *= i
#         i=1
#     i+=1

# print(first)
# print(second)
# print(sum * first * second)

#최소 공배수
# number1 = int(input("첫번째 수: "))
# number2 = int(input("두번째 수 : "))

# data1 = []
# data2 = []

# for i in range(1, number2+1): # 첫번째 배수를 구함
#   data1.append(i*number1)
# for i in range(1, number1+1): # 두번째 배수를 구함
#   data2.append(i*number2)

# for i in data1: # 첫번째 배수와 두번째 배수가 같은 것 중 가장 작은 값 추출
#   if i in data2: 
#     lcm = i
#     break

# print("최소공배수", lcm)


def calculate(num1, num2):
    i = 1
    sum = 1
    while (i != num1+1):
        if num1 % i == 0 and num2 % i == 0:
            # print('i:', i)
            num1 //= i
            num2 //= i 
            sum *= i
            i=1
        i+=1
    return sum, num1, num2

n1, n2 = map(int, input().split())

if n1 <= n2:
    num1 = n1
    num2 = n2
else:
    num1 = n2
    num2 = n1   

sum, num1, num2 = calculate(num1, num2)

print(sum, sum*num1*num2)