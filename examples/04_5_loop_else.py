# 4.5 루프의 else 절 예제

# 소수 판별: break 없이 루프가 끝나면 else 실행
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # break 없이 루프가 끝났을 때 실행
        print(n, 'is a prime number')
