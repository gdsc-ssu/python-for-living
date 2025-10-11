- 컴프리헨션 활용법 (리스트, 딕셔너리, 셋)

컴프리헨션

→ 코드 간결, 가독성 높아짐

**리스트 컴프리헨션**

- 기본 구조

[expression for item in iterable if condition]

1. expression : 리스트에 담을 값을 정의하는 부분
2. for item in iterable : 리스트 컴프리헨션이 적용될 값을 정의
    
    2-1. iterable : 순회 가능한 객체 [리스트, 튜플]
    
    2-2. 객체에서 반복되는 요소를 받는 변수
    
3. if condition : 선택적으로 각 item이 이 조건을 만족할 때만 리스트에 포함
- 특징
1. 간단한 반복문 처리
2. 조건문을 통한 필터링
3. 중첩된 반복문 처리
4. 함수 호출과 함께 사용

```python
#기존 반복문을 사용한 리스트 작성
square = []
for x in range(10):
	squares.append(x**2)
print(squares)

#리스트 컴프리헨션을 사용한 리스트 생성
squares_comp = [x**2 for x in range(10)]
print(squares_comp)
```

[https://hobbylife.tistory.com/entry/리스트-컴프리헨션-구조와-사용방법-초보자를-위한-간단한-설명과-예제#google_vignette](https://hobbylife.tistory.com/entry/%EB%A6%AC%EC%8A%A4%ED%8A%B8-%EC%BB%B4%ED%94%84%EB%A6%AC%ED%97%A8%EC%85%98-%EA%B5%AC%EC%A1%B0%EC%99%80-%EC%82%AC%EC%9A%A9%EB%B0%A9%EB%B2%95-%EC%B4%88%EB%B3%B4%EC%9E%90%EB%A5%BC-%EC%9C%84%ED%95%9C-%EA%B0%84%EB%8B%A8%ED%95%9C-%EC%84%A4%EB%AA%85%EA%B3%BC-%EC%98%88%EC%A0%9C#google_vignette)

**딕셔너리 컴프리헨션**

- 기본 구조

{키_표현식 : 값_표현식 for 변수 in 반복가능한객체}

1. 키_표현식 : 새로운 딕셔너리의 키를 정의하는 표현식
2. 값_표현식 : 해당 키에 대한 값을 정의하는 표현식
3. 변수 : 순회 가능한 객체에서 하나씩 요소를 가져오는 변수

```python
numbers=[1,2,3,4,5,6,7,8,9,10]
squares_dic = {x: x**2 for x in numbers}
```

https://olivia-blackcherry.tistory.com/165

**셋 컴프리헨션**

- 기본 구조

{표현식 for 표현식 in 순회가능객체}

- 특징
1. 중복 제거

```python
    my_list = [1, 2, 2, 3, 4, 4, 5]
    my_set = {x for x in my_list}
   
```

```python
a_set = { n for n in range(10) if n%2==1}
```
