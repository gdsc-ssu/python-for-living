# 4.4 break와 continue 문 예제

# break 예시: 소인수 찾기
print("=== break 예시 ===")
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} equals {x} * {n//x}")
            break

print()

# continue 예시: 짝수/홀수 구분
print("=== continue 예시 ===")
for num in range(2, 10):
    if num % 2 == 0:
        print(f"Found an even number {num}")
        continue
    print(f"Found an odd number {num}")
