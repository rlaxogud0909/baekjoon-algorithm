# 알아야 할것
# 파이썬 내장 함수 -> islower(), isupper(), isdigit(), isspace()
# stirng ->string.ascii_uppercase, string.digits, string.ascii_lowercase ..

# import string

# s = "This is String1111"

# for i in s:
#     print(i)
#     if i == " ":
#         print('공백')
#     elif i in string.digits:
#         print('숫자')
#     elif i == i.upper():
#         print("대 문자")
#     elif i == i.lower():
#         print("소문자")

import string
import sys



while(True):
    null = 0
    upper = 0
    lower = 0
    digit = 0
    s = sys.stdin.readline().rstrip("\n")

    if not s:
        break
    for i in s:
        if i.isspace():
            null +=1
        elif i in string.digits:
            digit += 1
        elif i in string.ascii_uppercase:
            upper += 1
        elif i in string.ascii_lowercase:
            lower += 1

    print(lower, upper, digit, null)
