# 4.3 range() 함수 예제

print("range(5):", list(range(5)))
print("range(5, 10):", list(range(5, 10)))
print("range(0, 10, 3):", list(range(0, 10, 3)))
print("range(-10, -100, -30):", list(range(-10, -100, -30)))

print()

# enumerate() 활용
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i, v in enumerate(a):
    print(i, v)

print()

# 이터러블을 인자로 받는 함수와 함께 사용
print("sum(range(4)):", sum(range(4)))
