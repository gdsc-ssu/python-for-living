# 기본 언패킹
a, b, c = (10, 20, 30)
print(a, b, c)  # 10 20 30

# 가변인자 언패킹
x, *y, z = [1, 2, 3, 4, 5]
print(x, y, z)  # 1 [2, 3, 4] 5

# 함수 호출 시 언패킹
def f(p, q, r):
    return p + q + r

nums = (4, 5, 6)
print(f(*nums))

# 키워드 인자 언패킹
d = {'p': 1, 'q': 2, 'r': 3}
print(f(**d))  # 6

# 딕셔너리 병합 언패킹
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3}
d_merged = {**d1, **d2}
print(d_merged)