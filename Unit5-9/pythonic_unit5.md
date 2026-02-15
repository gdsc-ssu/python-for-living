### 1. 리스트 더 보기

```python
list.append(x) # 리스트의 끝에 항목을 더함
list.extend(iterable) # 리스트 끝에 이터러블의 모든 항목을 덧붙임
list.insert(i,x) # 첫 번째 인자는 인덱스 주어진 인덱스 위치에 항목(x)을 삽입
list.remove(x) # 리스트에서 값이 x와 같은 첫 번째 항목 제거
list.pop([i]) # 리스트에서 주어진 위치의 항목 제거 후 돌려줌. 인덱스 없을 땐 마지막 항목을 삭제
list.clear() # 리스트의 모든 항목 삭제
list.index(x[,start[, end]]) # 선택적 인자 start와 end는 슬라이스 표기법 해석, 검색을 리스트의 특별한 서브 시퀀스로 제한하는데 사용
list.count(x) # 리스트에서 x가 등장하는 횟수
list.sort(*,key=None,reverse=False) # 리스트의 항목들을 제자리에서 정렬
list.reverse() # 리스트의 요소들을 제자리에서 뒤집음
list.copy() # 리스트의 사본 돌려줌
```

- insert, remove, sort 같은 메서드들은 리스트를 수정,  반환 값 출력X. 기본 None을 돌려줌 ( 파이썬 모든 가변 자료 구조에 적용되는 설계 원리)
- 서로 다른 형 끼리는 비교할 수 없기에 정렬 등 불가능

```python
stack = [3,4,5]
stack.append(6)
stack.pop()
```

- 리스트를 스택으로 사용하기

```python
from collections import deque
queue=deque(["A","B","C"])
queue.append("D")
queue.popleft()
```

- 리스트를 큐로 사용하기

```python
squares = []
for x in range(10):
		squares.append(x**2)

squares = list(map(lambda x:x**2,range(10)))

squares = [x**2 for in x in range(10)]
```

- 리스트 컴프리헨션 : 리스트를만드는 간결한 방법 제공. 다른 시퀀스나 이터러블 멤버에 연산을 적용한 결과 리스트를 만들거나 어떤 조건을 만족하는 요소들로 구성된 서브 시퀀스를 만드는 것.
- 리스트 컴프리헨션은 표현식과 for또는 if 절을 감싸는 대괄호로 구성.

```python
vec = [-4, -2, 0, 2, 4]
# 값을 두배로 하여 새 리스트를 만듭니다
[x*2 for x in vec]

# 음수를 제외하도록 리스트를 필터링합니다
[x for x in vec if x >= 0]

# 모든 요소에 함수를 적용합니다
[abs(x) for x in vec]

# 각 요소에 메서드를 호출합니다
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
[weapon.strip() for weapon in freshfruit]

# (숫자, 제곱) 과 같은 2-튜플의 리스트를 만듭니다
[(x, x**2) for x in range(6)]

# 튜플은 괄호로 묶어야합니다, 그렇지 않으면 에러가 발생합니다
[x, x**2 for x in range(6)]
  File "<stdin>", line 1
    [x, x**2 for x in range(6)]
     ^^^^^^^
```

- 표현식이 튜플이면 반드시 괄호로 둘러싸야 함

```python
from math import pi
[str(round(pi,i)) for i in range(1,6)]

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

[[row[i] for row in matrix] for i in range(4)]

# 복잡한 흐름문보다 내장 함수 선호 zip() 사용 가능
list(zip(*matrix))
```

- 복잡한 표현식과 중첩된 함수들 포함 가능

### 2. del 문

- 객체 자체를 삭제하는 키워드

```python
a=[1,2,3,4,5,6,7,8,9]
del a[0] # [2,3,4,5,6,7,8,9]
del a[2:4] # [2,3,6,7,8,9]
del a[:] # []

del a # 리스트 a를 비우는 것이 아닌 변수 이름 a 자체를 삭제
```

| 구분 | del | pop() |
| --- | --- | --- |
| 삭제 기준 | 인덱스 | 인덱스 |
| 반환값 | X | 삭제한 값 반환 |
| 슬라이스 삭제 | 가능 | X |
| 변수 자체 삭제 | 가능 (del a) | X |

### 3. 튜플과 시퀀스

- 시퀀스 자료형 : 리스트와 문자열 그리고 튜플

```python
t = 12345, 54321, 'hello!'

# 튜플은 중첩될 수 있음
u = t, (1, 2, 3, 4, 5)
u # ((12345, 54321, 'hello!'),(1, 2, 3, 4, 5))

# 튜플은 불변
t[0] = 88888 # -> error

# 하지만 가변 객체를 포함할 수 있음
v = ([1, 2, 3], [3, 2, 1])

# 빈 튜플
empty=()
# 하나의 항목으로 구성된 튜플은 값 뒤에 쉼표 붙여서 만듦
singlton = 'hello',

```

- 튜플은 항상 괄호에 둘러 쌓여 출력되지만 괄호 없이 입력될 수 있음. 튜플은 불변이고 언 패킹이나 인덱싱으로 액세스함. 그러나 리스트는 가변에 이터레이션으로 액세스
- t = 12345,54321,’hello!’ 는 튜플 패킹의 예
- x, y, z = t 는 시퀀스 언 패킹이라 불림. 좌변에시퀀스에 있는 요소들과 같은개수의 변수드링 올 것을 요구

### 4. 집합

- 중괄호나 set() 함수 사용 가능

```python
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# 중복은 제거됨

'orange' in basket # True
'crabgrass' in basket # False

# 두 단어의 고유한 글자들로 집합 연산 시연

a = set('abracadabra')
b = set('alacazam')

a - b # a 에 있으나 b 에 없는 글자들
a | b # a 나 b, 혹은 양쪽 모두에 있는 글자들
a & b # a 와 b 모두에 있는 글자들
a ^ b # a 나 b 에 있지만 양쪽 모두에 있지는 않은 글자들

a = {x for x in 'abracadabra' if x not in 'abc'}
# 집합 컴프리헨션도 지원
```

- 빈 집합을 만드려면 set()

### 5. 딕셔너리

- 키(key) : 값(value)
- 시퀀스 타입, 인덱스로 접근하는 리스트와 튜플과 다르게 딕셔너리는 키를 기반으로 접근하는 매핑 타입
- key 는 반드시 불변 객체 (문자열, 숫자, 튜플(내용도 모두 불변인))

```python
d = {} # 빈 딕셔너리

d={"a":1,"a":2} # 키는 중복 불가능, 기존 값을 덮어씀
-> {"a":2}

d["name"]="철수" # 값 저장
d["name"] # 값 가져오기
del d["name"] # 삭제

dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
# dict() 생성자는 키-값 쌍들의 시퀀스로부터 딕셔너리 구성

{x: x**2 for x in (2, 4, 6)}
# 딕셔너리 컴프리헨션 가능
```

- 존재하지 않는 키 접근 시 keyError
- get() 으로 접근하면 에러가 아닌 None 출력
- list(d) : 딕셔너리에 사용되고 있는 모든 리스트를 삽입 순서대로 돌려줌
- sorted(d) : 정렬
- 하나의 키가 딕셔너리에 있는지 검사하려면 in 키워드

### 6. 루프 테크닉

```python
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)
  
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)
```

- 딕셔너리로 루핑할 때, items() 메서드를 통해 대응하는 값을 얻을 수 있음
- enumerate() 함수를 사용하면 위치 인덱스와 대응 값 얻을 수 있음
- zip() 함수로 둘 이상의 시퀀스 동시 루핑 가능
- reversed() 함수로 시퀀스 거꾸로 루핑
- sorted() 함수로 정렬된 새 리스트 받기
- set() 사용하면 중복 요소 제거

### 7. 조건 더 보기

- not 이 가장 높은 우선순위, or이 가장 낮은 우선순위
    - A and not B or C == (A and (not B)) or C
- 논리 연산자 and와 or 는 소위 단락 회로 연산자

### 8. 시퀀스와 다른 형들 비교하기

- 비교는 사전식 순서를 사용
- 어느 한 시퀀스가 소진될 때까지 계속함

```python
(1, 2, 3)              < (1, 2, 4)
[1, 2, 3]              < [1, 2, 4]
'ABC' < 'C' < 'Pascal' < 'Python'
(1, 2, 3, 4)           < (1, 2, 4)
(1, 2)                 < (1, 2, -1)
(1, 2, 3)             == (1.0, 2.0, 3.0)
(1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)
```