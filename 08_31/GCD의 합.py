# 4, 10, 20, 30, 40
# 10,20,30,40의 쌍을 구해야함 

def gcd(a, b):
    n, m = a, b
    while m != 0:
        n = n%m
        m, n = n, m

    return n

# 풀이1) 런타임 에러
# n = int(input())
# n_list = []
# for i in range(3):
#     n_list.append(list(map(int, input().split())))

# # print(n_list)

# for t in range(n):
#     sum = 0
#     for j in range(n_list[t][0]-1):
#         for i in range(j+1, n_list[t][0]):
#             sum += gcd(n_list[t][j+1], n_list[t][i+1])
#             # print(gcd(n_list[t][j+1], n_list[t][i+1]))

#     print(sum)


# 풀이2)
for t in range(int(input())):
    n_list = list(map(int, input().split()))
    sum = 0
    for j in range(n_list[0]-1):
        for i in range(j+1, n_list[0]):
            sum += gcd(n_list[j+1], n_list[i+1])
            # print(gcd(n_list[t][j+1], n_list[t][i+1]))
    print(sum)