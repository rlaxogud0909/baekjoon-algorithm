#https://www.acmicpc.net/problem/1935

# 후위 표기식을 만드는 코드
# 123*+45/-

n = int(input())
ss = list(input())
result = []
alpha = [0]*n
for i in range(n):
    alpha[i] = int(input())

for s in ss:
    if s.isalpha():
        result.append(alpha[ord(s)-ord('A')])
        # print(result)
    else:
        # print('s :', s)
        # print(result)
        n1 = result.pop()
        n2 = result.pop()
        if s == '+':
            result.append(n2+n1)
        elif s == '-':
            result.append(n2-n1)
        elif s == '*':
            result.append(n2*n1)
        elif s == '/':
            result.append(n2/n1)
print('%.2f' %result[0])
