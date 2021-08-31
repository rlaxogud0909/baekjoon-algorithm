# 2진수가 주어졌을 때 8진수로 변환 -> 2의 3승이니까 3로 쪼갬
# 11001100 ->   11  / 001 / 100 -> 314


# n = list(input())
# n.reverse()

# print(n)

n = input()
n_r = n[::-1]

stack=[]

if len(n_r) % 3 != 0:
    last = len(n_r) % 3
    n_r_3 = n_r[:-last]
    s = n_r[-last:] 

# print(n_r_3)

result = []

for i in range(0, len(n_r_3), 3):
    # print('i:', i)
    a, b, c=int(n_r_3[i])*1, int(n_r_3[i+1])*2, int(n_r_3[i+2])*4
    result.append(str(a+b+c))

# print(result)

if last > 0:
    sum = 0
    for i in range(len(s)):
        sum += int(s[i])*(2**i)
        
print(sum, end="")
result.reverse()
print("".join(result))

## 위의 코드 런타임 에러 ##

# oct 함수 사용
print(oct(int(input(), 2))[2:])