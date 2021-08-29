n = int(input())

sum = 1
cnt = 0
for i in range(1, n+1):
    sum *= i

sum = list(str(sum))

for i in reversed(sum):
    if i == '0':
        cnt += 1
    else:
        break

print(cnt)

# counter 함수 이용??