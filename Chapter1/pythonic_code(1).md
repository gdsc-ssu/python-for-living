## 1. 컴프리헨션 문법
> 파이썬의 자료구조 데이터를 **간결하게** 생성할 수 있는 문법

### 리스트 컴프리헨션
> 리스트를 만드는 간결한 방법을 제공

```python
numbers = []
for i in range(5):
    numbers.append(i*2)

#컴프리헨션 표현
numbers = [i*2 for i in range(5)]
# [0, 2, 4, 6, 8]

#조건문을 넣어도 됨
even = [i for i in range(10) if i % 2 == 0]
# [0, 2, 4, 6, 8]

#if 중첩도 가능
data = [i for i in range(1,11) if i % 2 == 0 if i<5]
# [0, 2, 4]
```

```python
date = [(x,y) for x in range(1,6) for y in range(1,4)]

# for 문과 비교
date2 = []
for i in range(1,6):
    for j in range(1,4):
        data2.append((i,j))

# [(1, 1), (1, 2), (1, 3), 
# (2, 1), (2, 2), (2, 3), 
# (3, 1), (3, 2), (3, 3), 
# (4, 1), (4, 2), (4, 3), 
# (5, 1), (5, 2), (5, 3)]
```

### 딕셔너리 컴프리헨션

**유의할 점 : for문 앞에 키:값을 적는다는 것과 대괄호가 중괄호로 바뀐 것**

```python
squares = [x: x**2 for x in range(5)]
# {0:0, 1:1, 2:4, 3:9, 4:16}
```

zip 함수 결합
```python
name = ["왕춘삼", "김덕팔", "황갑득"]
age = [23, 14, 42]

data = {key: value for (key, value) in zip(name, age) if value > 20}

# 출력결과
{'왕춘삼': 23, '황갑득': 42}
```

### 셋(집합) 컴프리헨션

**유의할 점 : 딕셔너리 컴프리헨션과 비슷, 키:값 형태가 아닌 것만 유의**

```python
unique = {x%3 for x in range(10)}
# {0, 1, 2}
```

- 반복문 + 조건문을 한 줄로 표현가능
- 가독성과 효율성 향상
- **단, 복잡한 로직은 가독성을 해침**


참고 문서
https://tibetsandfox.tistory.com/25
