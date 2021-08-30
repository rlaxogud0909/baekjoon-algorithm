# n -> a ~ m -> z

n = list(input())

# for i in n:
#     print(chr(ord(i)-13), end='')

for i in n:
    if i == " ":
        print(" ", end="")
    if i.isdigit():
        print(i, end="")

    if 'a' <= i <= 'z':
        if ord(i)-13 < ord('a'):
            n = ord(i)-ord('a')
            nn = 12 - n
            print(chr(ord('z')-nn), end="")
        else:
            print(chr(ord(i)-13), end="")
    
    elif 'A' <= i <= 'Z':
        if ord(i)-13 < ord('A'):
            n = ord(i)-ord('A')
            nn = 12 - n
            print(chr(ord('Z')-nn), end="")
        else:
            print(chr(ord(i)-13), end="")



# print(chr(ord('B')-13))

# print(ord('B'))