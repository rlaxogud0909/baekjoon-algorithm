# < > 안의 뒤집어 지지 않는다.

import sys
word = list(sys.stdin.readline().rstrip())
result = ""
sum = ""
start = False
# print(word)

for i in range(len(word)):
    if start == False:
        if word[i] == '<':
            start = True # '<'를 시작할때
            result += word[i]
        # 공백이 나오면 sum에 넣어줌, result 초기화
        elif word[i] == " ":
            result += word[i]
            sum += result
            result = ""
        # <>밖의 단어 뒤집으면서 넣음
        else:
            result = word[i] + result
        
    else:
        result += word[i]
        if word[i] == ">":
            start = False # '>'로 끝날때
            sum += result
            result = ""


print(sum+result)