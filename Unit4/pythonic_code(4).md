### 9. 함수 정의 더 보기

**(1) 기본 인자 값 parameter default value** 

- 디폴트 값, 함수 정의 시점에 정의되고 있는 스코프에서 구해짐.

```python
i = 5

def f(arg=i):
    print(arg)

i = 6
f()
# 5
```

- 기본값은 한 번만 값이 구해진다. 리스트나 딕셔너리 같은 가변 객체가 차이를 가짐

```python
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

# [1]
# [1, 2]
# [1, 2, 3]
```

- L=None 으로 쓰면 기본값이 공유되지 않음
- 기본 매개변수를 항상 앞에 배치해야 함


**(2) 키워드 인자**

- 함수는 kwarg=value 형식의 키워드 인자를 사용해 호출될 수 있음

```python
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):

# 옳은 호출
parrot(1000)                                          # 1개의 위치 인자
parrot(voltage=1000)                                  # 1개의 키워드 인자
parrot(voltage=1000000, action='VOOOOOM')             # 2개의 키워드 인자
parrot(action='VOOOOOM', voltage=1000000)             # 2개의 키워드 인자
parrot('a million', 'bereft of life', 'jump')         # 3개의 위치 인자
parrot('a thousand', state='pushing up the daisies')  # 1개의 위치, 1개의 키워드

# 틀린 호출
parrot()                     # 필수 인자 누락
parrot(voltage=5.0, 'dead')  # 키워드 인자 뒤에 키워드가 아닌 인자가 옴
parrot(110, voltage=220)     # 같은 인자가 중복됨
parrot(actor='John Cleese')  # 알려지지 않은 키워드 인자
```

- 키워드 인자는 위치 인자 뒤에 와야함

```python
f(1,2,c=3)  # 가능
f(a=1,2)  # 불가능
```

- 키워드 인자의 순서는 중요하지 않음
- 필수 인자도 키워드 인자로 전달할 수 있고 어떤 인자도 두 개 이상의 값을 받을 수 없음
- **name 형식은 *name 형식 다음에 와야함
- **name 형식의 마지막 형식 매개변수가 존재하면 형식 매개변수들에 대응하지 않는 모든 키워드 인자를 담은 딕셔너리를 받음


**(3) 특수 매개 변수**

인자는 위치나 명시적 키워드로 함수에 전달될 수 있음. 인자의 전달 방법을 제한할 수 있다.

```python
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      -----------    ----------     ----------
        |             |                  |
        |        위치-키워드                  |
        |                                - 카워드 전용
         -- 위치 전용

```

- 위치-키워드 인자 : / 와 * 이 없으면 인자를 위치나 키워드로 함수에 전달 가능
- 위치 전용 매개 변수 : / 앞에 놓임. 위치 전용 매개 변수를 나머지 매개 변수들로부터 논리적 분리하는데 사용. 위치 전용이면 매개변수 순서가 중요하고 키워드로 매개변수 전달 불가
- 키워드 전용 인자 : 매개변수를 키워드 전용으로표시하기 위해 첫 번째 키워드 전용 매개 변수 바로 전에 인자 목록에 * 를 넣는다

```python
def standard_arg(arg): # 제한 X
    print(arg)

def pos_only_arg(arg, /): # 위치 전용
    print(arg)

def kwd_only_arg(*, arg): # 키워드 전용
    print(arg)

def combined_example(pos_only, /, standard, *, kwd_only): # 세 가지 호출 규칙 모두 사용
    print(pos_only, standard, kwd_only)
```

- 위치 인자 name과 name을 키로 가지는 **kwds 사이에 잠재적 충돌이 있는 경우를 고려

```python
def foo(name, **kwds):
    return 'name' in kwds
    
# foo(1,**{'name':2}) 호출 시
# foo(name=1, name=2)
=> 같은 name에 두 번 값 전달 -> 에러

# 해결 : foo(name,/,**kwds):
```

- name 키워드는 항상 첫 번째 매개 변수에 결함하므로, True 반환 불가. ‘name’ 키가 **kwds로 절대 가지 못해서 항상 ‘name’ in kwds 가 False 라는 것
- 위치 전용 인자 / 를 사용하여 해결
- API의 경우 비호환 API 변경 발생 방지 위해 위치 전용 사용 지향


**(4) 임의의 인자 목록**

- 가변 위치 인자와 키워드 전용 인자
- *args : 나머지 모든 위치 인자들 → 튜플로 형태로 args에 저장
- **kwargs : 나머지 모든 키워드 인자들 → 딕셔너리 형태로 kwargs 에 저장

```python
def my_func(*args, **kwargs):
    print("Positional arguments:")
    for arg in args:
        print(arg)
    
    print("\nKeyword arguments:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# 위치 인자와 키워드 인자를 함께 사용하는 경우
my_func(1, "apple", name="John", age=30)

# 결과
# Positional arguments:
# 1
# apple

# Keyword arguments:
# name: John
# age: 30

# 위치 인자만 사용하는 경우
my_func("banana", "orange", "kiwi")

# 결과
# Positional arguments:
# banana
# orange
# kiwi

# 키워드 인자만 사용하는 경우
my_func(color="red", size="medium")

# 결과
# Positional arguments:

# Keyword arguments:
# color: red
# size: medium
```


**(5) 인자 목록 언 패킹**

- 분리된 위치 인자들을 요구하는 함수 호출 시 언 패킹 해야하는 상황 발생
- range() 함수는 start, stop 인자가 그 예
- 리스트와 튜플로부터 인자 언패킹 위해 *연산자 사용
- 딕셔너리는 ** 연산자 사용

```python
args = [3, 6]
list(range(*args))            # 리스트에서 언패킹된 인자로 호출
[3, 4, 5]

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)
```


**(6) 람다 표현식**

- lambda 키워드를 통해 이름 없는 함수 만들 수 있음. 문법적으로 하나의 표현식으로 제한, 둘러싸는 스코프에 있는 변수들을 참조할 수 있음

```python
def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
f(0) #42
f(1) #43
```

- list.sort() 에도 활용

```python
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
# pair[1] 을 기준으로 정렬하라
```


**(7) 도큐멘테이션 문자열 (독스트링)**

- 첫 줄은 객체의 목적을 짧게, 간결 요약, 대문자 시작, 마침표 종료
- 여러 줄이라면 두번 째 줄을 비워 요약과 설명을 분리

(8) 함수 어노테이션

- 함수 어노테이션 : 사용자 정의 함수가 사용하는 형들에 대한 선택적인 메타데이터 정보
- f.__annotations__ 에 저장
- -> : 반환 어노테션

```python
def f(ham: str, eggs: str = 'eggs') -> str:
# ham : str 기대
# eggs : str 기대
# -> : str 반환 기대
```

참고 자료
https://wikidocs.net/22799
https://python101.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%ACPython%EC%9D%98-%EC%9E%84%EC%9D%98%EC%9D%98-%EC%9D%B8%EC%9E%90%EB%AA%A9%EB%A1%9Dvariadic-arguments-%EC%97%90-%EB%8C%80%ED%95%B4%EC%84%9C
https://wikidocs.net/22801

