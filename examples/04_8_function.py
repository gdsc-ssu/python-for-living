# 4.8~4.9 함수 정의 예제


# 피보나치 수열 출력
def fib(n):
    """n 보다 작은 피보나치 수열을 인쇄합니다."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


# 피보나치 수열 리스트 반환
def fib2(n):
    """n 보다 작은 피보나치 수열 리스트를 반환"""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result


print("=== 피보나치 출력 ===")
fib(2000)
print("=== 피보나치 리스트 ===")
print(fib2(100))

print()

# 함수는 일급 객체
f = fib
f(100)

print()


# 기본 인자 값 주의: 가변 객체 공유 문제
def f_wrong(a, L=[]):
    L.append(a)
    return L


def f_correct(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


print("=== 기본 인자 값 주의 ===")
print("잘못된 예시:", f_wrong(1), f_wrong(2), f_wrong(3))
print("올바른 예시:", f_correct(1), f_correct(2), f_correct(3))

print()


# 임의의 인자 목록
def concat(*args, sep="/"):
    return sep.join(args)


print("=== 임의의 인자 목록 ===")
print(concat("earth", "mars", "venus"))
print(concat("earth", "mars", sep="."))

print()


# 인자 목록 언패킹
print("=== 언패킹 ===")
args = [3, 6]
print(list(range(*args)))

d = {"voltage": "four million", "state": "bliss"}
print(d)

print()

# 람다 표현식
print("=== 람다 ===")
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)

print()


# 함수 어노테이션
def greeting(ham: str, eggs: str = 'eggs') -> str:
    return ham + ' and ' + eggs


print("=== 함수 어노테이션 ===")
print(greeting('spam'))
print("annotations:", greeting.__annotations__)
