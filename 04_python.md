# 4. 기타 제어 흐름 도구

Status: Done

# **4. 기타 제어 흐름 도구**

### **4.1. if 문**

```python
if (조건문) :
	(실행문1)
	(실행문2)
	....
elif (조건문):
	(실행문)
else (조건문):
	(실행문)
```

elif == else if

### 4.2 for 문

: 임의의 시퀀스(리스트,문자열)의 항목들을 그 시퀀스에 들어있는 순서대로 이터레이션함

: 컬렉션을 이터레이트 하는 동안 같은 컬렉션을 수정하는 코드는 올바르게 동작하도록 만들기 힘듦 

→ **컬렉션의 복사본으로 루프 만듦**

→ **새 컬렉션을 만듦**

```python
# 샘플 컬렉션을 만듭니다
users = {'Hans': 'active', 'Éléonore': 'inactive', '홍길동': 'active'}

# 전략:  사본을 이터레이트
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# 전략:  새 컬렉션 만들기
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
```

### 4.3 range() 함수

: 숫자들의 시퀀스로 이터레이트

```python
range(5,10)
#5~9
range(0,10,3)
#0 3 6 9 
range(-10,-100,-30)
#-10 -40 -70
```

: 시퀀스의 인덱스들로 이터레이트

→ range() && len()

```python
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])
    
#0 Mary
#1 had 이런식으로 감
```

⇒enumerate(iterable, start=0) 사용이 더 편함

```python
a = ['Mary', 'had', 'a', 'little', 'lamb']
list(enumerate(a))
```

**범위 그냥 인쇄 시, 이상한 일 일어남

```python
range(10)
#출력
#range(0,10)
```

→ range()가 돌려준 객체는 리스트인 것 같지만 리스트 아님 , 실제로 리스트 만들지 않음

⇒ 이런 객체 == 이터러블

### 4.4 break와 continue 문

break : 가장 가까이 둘러싸는 for나 while 루프로부터 빠져 나감

continue : 루프의 다음 이터레이션에서 계속하도록 만듦

### **4.5 루프의 else절**

loop가 break가 실행되지 않은 채 종료되면 else절이 실행됨

1. for : break가 실행 x → else절 실행 : loop가 마지막 이터레이션을 돌면
2. while : loop의 상태가 false가 되면 → else절 실행  

**return 이나 예외 발생 시, else절 실행 안됨

```python
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # 루프에서 인수를 발견하지 못하고 떨어짐
        print(n, 'is a prime number')
#else절은 if문이 아니라 for루프에 속함
```

### 4.6 pass 문

pass : 아무것도 하지 않음

```python
def initlog(*args):
    pass   # 구현을 잊지마세요!
```

→ `pass` 대신 `…` 사용

### 4.7 match 문

```python
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418 | 999: # | (or) 사용 가능
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
            #와일드카드(like default)
```

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")
```

→ 생성자 같이 사용 가능

```python
class Point:
    __match_args__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y

match points:
    case []:
        print("No points")
    case [Point(0, 0)]:
        print("The origin")
    case [Point(x, y)]:
        print(f"Single point {x}, {y}")
    case [Point(0, y1), Point(0, y2)]:
        print(f"Two on the Y axis at {y1}, {y2}")
    case _:
        print("Something else")
```

→ `__match_args__` : 위치 인자 → 순서(위치)만으로 매칭 가능

```python
match point:
    case Point(x, y) if x == y:
        print(f"Y=X at {x}")
    case Point(x, y):
        print(f"Not on the diagonal")
```

→ 가드 : 패턴 매칭 뒤에 `if` 문을 붙여 더 세밀한 조건을 걺

- 기타 주요 특징
    - 시퀀스 언패킹 / 패킹
    - 매핑(딕셔너리)
    - `as` 키워드: 패턴 매칭과 동시에 해당 객체 전체를 변수에 담고 싶을 때 사용
        
        ```python
        case (Point(x1, y1), Point(x2, y2) as p2): ...
        ```
        
    - 상수 매칭
        
        ```python
        from enum import Enum
        class Color(Enum):
            RED = 'red'
            GREEN = 'green'
            BLUE = 'blue'
        
        color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))
        
        match color:
            case Color.RED:
                print("I see red!")
            case Color.GREEN:
                print("Grass is green")
            case Color.BLUE:
                print("I'm feeling the blues :(")
        ```
        

### 4.8 함수 정의하기

```python
def fib(n):    # n 보다 작은 피보나치 수열을 씁니다
    """n 보다 작은 피보나치 수열을 인쇄합니다."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# 이제 방금 정의한 함수를 호출합니다:
fib(2000)
```

1. 함수 정의

def (함수명)(매개변수):

[들여쓰기하기] (함수 관련 문장들)

함수 이름을 현재 심볼 테이블의 함수 객체와 연결

→ 함수 바디의 첫문장: 선택적으로 문자열 리터럴 == 독스트링

1. 함수 실행

함수의 지역 변수들을 위한 새 심복 테이블 만듦

→ 함수에서의 모든 변수 대입들은 값을 지역 심볼 테이블에 저장

변수 참조 : 1.지역 심볼 테이블 → 2.전역 심볼 테이블→3.내장 이름들의 테이블

1. 함수 호출

전달되는 실제 매개변수들(인자들)은 호출될 때 호출되는 함수의 지역 심볼 테이블에 만들어짐

→ 인자들은 값에 의한 호출로 전달

```python
fib
f = fib
f(100)
#0 1 1 2 3 5 8 13 21 34 55 89
```

→ return문이 없는 함수도 값을 돌려줌 (None)

→ return문이 있는 함수는 함수로부터 값을 갖고 복귀하게 만듦

### 4.9 함수 정의 더보기

정해지지 않은 개수의 인자들로 함수를 정의하는 것도 가능 → 3가지 형식

**4.9.1 기본 인자 값**

: 하나 or 그 이상 인자들의 기본값을 지정하는 것

→ 정의된 것보다 더 적은 개수의 인자들로 호출될 수 있는 함수를 만듦 (디폴트 값)

```python
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes'}:
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
```

*in 키워드 : `x in s` : x가 s의 멤버일 때 `True`, 그렇지 않을 때 `False` 

**기본값은 오직 한 번만 값이 구해짐

```python
#기본값이 공유되는 것
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

#기본값이 공유되지 않는 것
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
```

**4.9.2 키워드 인자**

: 함수는 `kwarg=value` 형식의 키워드 인자를 사용해서 호출될 수 있습니다. 

```python
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
```

→ 필수인자 : `voltage` , 선택인자 : `state` , `action` , `type` 

- 가능한 호출 방법

```python
parrot(1000)                                          # 1개의 위치 인자
parrot(voltage=1000)                                  # 1개의 키워드 인자
parrot(voltage=1000000, action='VOOOOOM')             # 2개의 키워드 인자
parrot(action='VOOOOOM', voltage=1000000)             # 2개의 키워드 인자
parrot('a million', 'bereft of life', 'jump')         # 3개의 위치 인자
parrot('a thousand', state='pushing up the daisies')  # 1개의 위치, 1개의 키워드
```

- 올바르지 않은 호출 방법

```python
parrot()                     # 필수 인자 누락
parrot(voltage=5.0, 'dead')  # 키워드 인자 뒤에 키워드가 아닌 인자가 옴
parrot(110, voltage=220)     # 같은 인자가 중복됨
parrot(actor='John Cleese')  # 알려지지 않은 키워드 인자
```

→ 키워드 인자는 위치 인자 뒤에 나와야 함

*인쇄되는 키워드 인자들의 순서 함수 호출로 전달된 순서와 일치함이 보장됨에 주목

**4.9.3 특수 매개 변수**

```python
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
    """
    pos1, pos2: 위치 전용 

    pos_or_kwd: 위치 또는 키워드 

    kwd1, kwd2: 키워드 전용
    """
```

→ / 와 *는 선택적 

→ 없으면, 인자를 위치나 키워드로 함수에 전달

→ 있으면, (위치 전용 매개변수) / (위치-키워드 or 키워드 전용) 

            * (키워드 전용 매개변수)

```python
def standard_arg(arg):
    print(arg)

def pos_only_arg(arg, /):
    print(arg)

def kwd_only_arg(*, arg):
    print(arg)

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)
```

- 사용 지침
    - 매개 변수의 이름을 사용자가 사용할 수 없도록 하려면 위치 전용을 사용
        
        → 매개 변수 이름이 실제 의미가 없을 때, 함수가 호출될 때 인자의 순서를 강제하려고 할 때, 또는 일부 위치 매개 변수와 임의의 키워드를 받아들이고 싶을 때 유용
        
    - 이름이 의미가 있고 함수 정의가 이름을 명시적으로 지정함으로써 더 이해하기 쉬워지거나, 사용자가 전달되는 인자의 위치에 의존하지 못하도록 하려면 키워드 전용을 사용
    - API의 경우, 향후 매개 변수의 이름이 수정될 때 비호환 API 변경이 발생하는 것을 방지하려면 위치 전용을 사용

**4.9.4 인자 목록 언 패킹**

인자들이 이미 리스트나 튜플에 있지만, 분리된 위치 인자들을 요구하는 함수 호출을 위해 언 패킹 해야 하는 경우,내장 `range()`함수는 별도의 start와 stop 인자를 기대함.

그것들이 따로 있지 않으면, 리스트와 튜플로부터 인자를 언 패킹하기 위해 `*`-연산자를 사용해서 함수를 호출하면 됨.

딕셔너리도 `**` -연산자를 써서 키워드 인자를 전달할 수 있음.

```python
def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)
```

**4.9.5 람다 표현식**

: `lambda` 키워드 사용해서 작고 이름 없는 함수를 만들 수 있음

```python
def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
f(0)
#42
f(1)
#43
```

**4.9.6 도큐멘테이션 문자열**

관례:

첫 줄은 항상 객체의 목적을 짧고 간결하게 요약

도큐멘테이션 문자열에 여러 줄이 있다면, 두 번째 줄은 비어 있어서 시각적으로 요약과 나머지 설명을 분리해야 함

**4.9.7 함수 어노테이션**

: 사용자 정의 함수가 사용하는 형들에 대한 완전히 선택적인 메타데이터 정보

`__annotations__` : 어노테이션은 함수 속성에 딕셔너리 형태로 저장

→ 강제성 없는 참조용 주석

매개변수 어노테이션 정의 : 매개변수 이름 뒤에 콜론을 쓰고 그 뒤에 어노테이션 값을 평가하는 푱현식을 작성

반환 값 어노테이션 정의 : 매개변수 목록과 함수 정의를 끝내는 콜론 사이에 `->` 리터럴을 쓰고 표현식을 작성

```python
def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

f('spam')
```

### 4.10 코딩 스타일

대부분 프로젝트가 고수하는 스타일 가이드

→ PEP 8

중요 부분

- 들려 쓰기에 4-스페이스를 사용하고, 탭을 사용X
    
    4개의 스페이스는 작은 들여쓰기 (더 많은 중첩 도를 허락) 와 큰 들여쓰기 (읽기 쉬움) 사이의 좋은 절충 → 탭은 혼란을 일으키고, 없애는 것이 최선
    
- 79자를 넘지 않도록 줄 넘김
    
    → 이것은 작은 화면을 가진 사용자를 돕고 큰 화면에서는 여러 코드 파일들을 나란히 볼 수 있게 함
    
- 함수, 클래스, 함수 내의 큰 코드 블록 사이에 빈 줄을 넣어 분리
- 가능하다면, 주석은 별도의 줄로 넣기
- 독스트링을 사용
- 연산자들 주변과 콤마 뒤에 스페이스를 넣고, 괄호 바로 안쪽에는 스페이스를 넣지 말기 `a = f(1, 2) + g(3, 4)`.
- 클래스와 함수들에 일관성 있는 이름을 붙이기
    
    → 관례는 클래스의 경우 `UpperCamelCase`, 함수와 메서드의 경우 `lowercase_with_underscores`
    
    첫 번째 메서드 인자의 이름으로는 항상 `self`를 사용
    
- 여러분의 코드를 국제적인 환경에서 사용하려고 한다면 특별한 인코딩을 사용X
    
    → 어떤 경우에도 파이썬의 기본, UTF-8, 또는 단순 ASCII조차, 이 최선
    
- 다른 언어를 사용하는 사람이 코드를 읽거나 유지할 약간의 가능성만 있더라도, 식별자에 ASCII 이외의 문자를 사용X