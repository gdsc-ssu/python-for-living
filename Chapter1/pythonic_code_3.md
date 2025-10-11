- 매직 메서드 (`__str__`, `__repr__`, `__eq__` 등)

매직메서드

:파이썬에서 사용되는 특별한 메소드

== 스폐셜 메서드

== 던더 메서드

- `__str__`

: 객체를 문자열로 반환

: interface로서의 역할을 수행하기 위해 존재

→ 서로 다른 타입을 가진 데이터끼리 상화작용 할 때 문자열로 변환시킴으로서 상호간의 호환이 가능

→ 사용자에 초점

```python
#print 내부적으로 str 메서드 호출
a = 1
b = 'hi'
c = [1,2,3]

print(a,b,c)
```

- `__repr__`

: 객체를 문자열로 반환

→객체를 문자열로 표현하기 위해 존재

→ 반환값은 eval 함수에 사용 가능, 새로운 객체 생성 가능 ( str의 경우 eval 사용 안됨)

→ print() 함수가 `__str__` 메서드를 찾지 못할 때 자동으로 호출

→ 개발자에 초점

- `__eq__`

: 비교 매직 메서드

→ x == y 를 판단하는 기준을 정의 (**eq**ual to → **eq**)

```python
class Str_Comparison(str):
    def __new__(cls, string):
        return super(Str_Comparison, cls).__new__(cls, string)
    def __lt__(self, other):
        return len(self) < len(other)
    def __le__(self, other):
        return len(self) <= len(other)
    def __gt__(self, other):
        return len(self) > len(other)
    def __ge__(self, other):
        return len(self) >= len(other)
    def __eq__(self, other):
        return len(self) == len(other)
    def __ne__(self, other):
        return len(self) != len(other)
        
s1 = Str_Comparison('Jane')
s2 = Str_Comparison('James')
s3 = Str_Comparison('Peter')
s4 = Str_Comparison('Elizabeth')

print(s1 < s2) # True
print('Jane' < 'James') # False

print(s2 == s3) # True
print('James' == 'Peter') # False

print(s3 < s4) # True
print('Peter' < 'Elizabeth') # False
```

https://tibetsandfox.tistory.com/39

[https://supermemi.tistory.com/entry/Python-3-Magic-Methods-다루기-2편-비교-연산자-eq-ne-lt-gt-le-ge#google_vignette](https://supermemi.tistory.com/entry/Python-3-Magic-Methods-%EB%8B%A4%EB%A3%A8%EA%B8%B0-2%ED%8E%B8-%EB%B9%84%EA%B5%90-%EC%97%B0%EC%82%B0%EC%9E%90-eq-ne-lt-gt-le-ge#google_vignette)