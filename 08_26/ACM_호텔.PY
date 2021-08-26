# n // h + 1 -> xxㅁ -> ㅁ 값

# n % h -> ㅁxx -> ㅁ 값

# 만약 n % h 가 0이라면? -> n//floor(꼭대기층) -> 층은 h로 꼭대기층

cnt = int(input())

for i in range(cnt):
    h, w, n = map(int, input().split())
    num = n//h + 1
    floor = n % h
    if n % h == 0: # 즉, 꼭대기 층일때
        num = int(n/h)
        floor = h
    print(f'{floor*100+num}')
