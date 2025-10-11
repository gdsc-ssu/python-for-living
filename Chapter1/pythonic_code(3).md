## 매직 메서드
> 클래스에 특수 동작을 정의하는 메서드 (자동 호출됨) / `__이름__` 형식

- `__str__` vs `__repr__`

```python
class User:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"User: {self.name}"     # print()용

    def __repr__(self):
        return f"User(name='{self.name}')"  # 개발자용 (디버깅)

user = User("Gahee")
print(user)      # User: Gahee
user             # User(name='Gahee')
```

→ print(user) → `__str__` 호출

→ user → `__repr__` 호출 : 대화형 콘솔 or Jupyter 등 

→ repr(user) → 명시적으로 `__repr__`  호출

→ str(user) → 명시적으로  `__str__` 호출

→  `__str__` 가 없으면 자동으로 `__repr__` 사용


- `__eq__` (== 비교 연산자 오버라이드)

```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

p1 = Point(1, 2)
p2 = Point(1, 2)
print(p1 == p2)  # True
```

→  a == b 를 하면, 내부적으로 호출

→ 클래스에 `__eq__`를 안 만들면 ==는 ‘객체가 같은 메모리 주소를 가리키는지’ 비교

- `__add__` : a + b 를 하면 내부적으로 실행
- `__len__` : len() 실행하면 내부에서 진짜 리스트의 길이를 반환