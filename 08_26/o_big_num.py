#  Ai의 오큰수는 오른쪽에 있으면서 Ai보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미

# [3, 5, 2, 7]

# NGE(1)-> 3의 오른쪽 5,2,7 중 가장 왼쪽에서 3보다 큰 5가 선택
# NGE(2)-> 5의 오른쪽 2,7 중 가장 왼쪽에 있는 3보다 큰 7이 선택
# NGE(3) -> 2의 경운 7
# NGE(7) -> 7보다 큰수 없거나 수가 없을때 -1 출력


# a_list = [3, 5, 2 ,7]
# a_list = [9, 5, 4, 8]
# A = [9, 5, 4, 8]

##########################################################
# 2중 for문 -> 시간 초과 발생

# import sys

# n = sys.stdin.readline()
# a_list = list(map(int, sys.stdin.readline().split()))
# result = []

# for i in range(len(a_list)):
#     for j in range(i, len(a_list)):
#         if a_list[i] < a_list[j]:
#             result.append(str(a_list[j]))
#             ok = True
#             break
#         ok = False
#     if ok == False:
#         result.append('-1')

# print(' '.join(result))
########################################################
# 시간 초과를 해결 하기 위해서 스텍을 쌓아서 풀어야함

# stack_index 안에 num의 index값을 넣어 차례대로 비교
# stack_index에 먼저 0을 넣어주고 i=1부터 시작해 넣어준다.

# 만약 스텍 인덱스가 없고, i<n 아니면 값을 출력한다.
# num[stack_index[-1]]로 num[i]를 비교하면서 num[i]가 크다면 
# result에 넣어주고 stack_index는 제거해준다.

n = int(input())
num = list(map(int, input().split()))

result = ['-1' for _ in range(n)]
stack_index = []
stack_index.append(0)
i=1

while stack_index and i<n:
    while stack_index and num[stack_index[-1]] < num[i]:
        result[stack_index[-1]] = str(num[i])
        stack_index.pop()
    
    stack_index.append(i)
    i += 1



res = " ".join(result)
print(res)

# print(result)