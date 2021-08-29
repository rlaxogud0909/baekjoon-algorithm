
result = []

n = input()


for i in range(len(n)):
    result.append(n[i:len(n)])

print(result)
result.sort()

for i in result:
    print(i)