### 7. match 문

```python
def http_error(status):
		match status:
				case 400:
						return "Bad request"
				case 401 | 403 | 404: **# | : or로 사용**
						return "Not allowed"
				case _: **# else 느낌, 나머지 부**
						return "Something's wrong with the internet"
				
```

튜플이랑 사용

```python
#point = (x,y) 튜플

match point:
		case(0,0):
				print("origin")
		case(0,y):
				print(f"Y={y}")
		case(x,0):
				print(f"X={x}")
		case(x,y):
				print(f"X={x}, Y={y}")
		case _:
				raise ValueError("Not a point")
				**# 의도적으로 에러를 발생시키는 예외 처리 문**
```

클래스랑 사용

```python
class Point:
		def __init__(self, x, y): # 생성자 역할
				self.x=x
				self.y=y

def where_is(point):
		match point:
				case Point(x=0,y=0):
						print("origin")
				case Point(x=0,y=y):
						print(f"Y={y}")
				case Point(x=x,y=0):
						print(f"X={x}")
				case Point(): # Point 객체면 매칭
						print("Somewhere else")
				case _:
						print("Not a point")
```

위치 기반

```python
class Point:
    __match_args__ = ('x', 'y') # 위치 기반 패턴 매칭
    # 위 문장이 있기 때문에 Point(0,0)이 가능한 것
    # 원래는 Point(x=0,y=0) 이라고 써야 했음  
    def __init__(self, x, y):
        self.x = x
        self.y = y

match points:
    case []: # 빈 리스트
        print("No points")
    case [Point(0, 0)]: # 리스트에 (0,0) 원소 하나
        print("The origin")
    case [Point(x, y)]: # 리스트에 (x,y) 원소 하나
        print(f"Single point {x}, {y}")
    case [Point(0, y1), Point(0, y2)]: # 리스트에 y축 위의 점 두개
        print(f"Two on the Y axis at {y1}, {y2}")
    case _: # 나머지
        print("Something else")
```

if 포함

```python
match point:
    case Point(x, y) if x==y:
        print(f"Y=X at {x}")
    case Point(x, y):
        print(f"Not on the diagonal")
```

- 시퀀스 패턴(리스트, 튜플 등) 은 매칭 가능
- iterator, string 은 매칭되지 않음
- 확장 언패킹 가능
    - [x, y, *rest], (x, y, *rest) ⇒앞에 x,y 저장 후 남은 요소들 rest 변수에 저장함
    - [x, y, *_] ⇒ 앞에 두개 요소만 필요하고 나머진 버림
- 딕셔너리 패턴 매칭 됨. 시퀀스와 다르게 extra key 허용
    - 언패킹 **rest 로 {”aaa” : b, **rest } ⇒ 나머지 키들 전부 rest 로 받음
    - **_ 는 문법적으로 틀림. ⇒ 어차피 무시하기 때문에 불필요
- as 키워드

```python
Point(x1,y1), Point(x2,y2) as p2
```

→ Point(x2,y2) as p2 : 이 객체를 분해해서 x2, y2도 쓰고 이 객체 자체를 p2로도 쓰겠다는 것.

- literal 비교 방식
    - 일반 리터럴 == 로 비교
    - True, False, None 은 예외로 is 사용. 프로그램 전체에서 단 하나의 객체만 존재하기 때문
    
    ```python
    x is True
    x is False
    x is None
    ```
    
- 이름 있는 상수 패턴

```python
from enum import Enum
# Enum : 의미 있는 상수 집합 정의
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

→ case RED : 라고 쓰면 RED라는 상수랑 비교하는게 아니고 RED 라는 변수에 바인딩된 것 (캡처 변수) 임.

그래서 [Color.RED](http://Color.RED) 라고 쓰는 것 → 상수 패턴으로 인식

- 이름 하나 = 캡처 변수 = 값을 변수에 저장하는 패
- dotted name = 상수