## 2. 언패킹(Unpacking)과 제너레이터(Generator)

### 언패킹
> 여러 값을 한 번에 변수에 풀어 넣는 기능

```python
a, b, c = [1, 2, 3]
print(a,b,c)
# 1 2 3

#리스트나 튜플 등 반복 가능한 객체면 다 가능
numbers = [1, 2, 3, 4, 5]
first, *middle, last = numbers
print(first, middle, last)
# 1 {2,3,4}, 5
```

### 제너레이터
>데이터를 필요할 때만 하나씩 생성하는 지연평가 방식 함수
```python
def count_up_to(n):
    for i in range(1,n+1):
        yield i

for num in count_up_to(5):
    print(num)
#1, 2, 3, 4, 5
```
함수 안에 yield 키워드를 사용하면 제너레이터이다.
yield가 값을 생성(반환)하고, 함수의 상태는 유지된 채 중단되었다가
다음 호출로 그 지점에서 재개된다.

yield 키워드
```python
def func():
    yield 1
    yield 2
    yield 3

foo = func()

print(next(foo)) # 1
print(next(foo)) # 2
print(next(foo)) # 3
```
### return 과의 차이점

제너레이터 함수는 yield 를 통해 값을 반환.
next 메소드나 for문 순회 등을 통해 값들을 리턴받을 수 있음.
**yield가 호출된다고 해서 함수가 종료되는 것은 아님**

제너레이터 내부에서 return을 사용하면 현재 값에 상관없이 StopIteration 예외 발생

```python
def func():
    print("1 리턴 전")
    yield 1
    print("1 리턴 후, 2 리턴 전")
    yield 2
    print("2 리턴 후, 3 리턴 전")
    yield 3
    print("3 리턴 후")


foo = func()

print(next(foo))
print(next(foo))
print(next(foo))

1 리턴 전
1
1 리턴 후, 2 리턴 전
2
2 리턴 후, 3 리턴 전
3
```


표현식 : 리스트 컴프리헨션과 동일하지만 **[] 대신 () 사용**
-> 값을 즉시 모두 만들지 않음

```python
lst=[x*2 for x in range(5)]
gen=(x*2 for x in range(5))
```

- 전체 시퀀스를 메모리에 올리지 않음 -> 큰 파일, 로그, 스트리밍 데이터 처리에 적합
- 필요할 때만 계산 -> 파이프라인에서 불필요한 계산 회피
- 로컬 변수로 상태를 유지하면서 반복 로직 구현 가능
- **디버깅 복잡, 한 번만 소비 가능. 다시 쓰려면 재생성**

참고 문서
https://tibetsandfox.tistory.com/28
