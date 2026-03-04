- 데코레이터 기초와 활용

**데코레이터**

: 함수나 메서드에 적용되어, 해당 함수나 메서드의 기능을 확장하거나 변경하는 역할

→ 기본적으로 함수를 인자로 받고 또 다른 함수를 반환하는 고차 함수

- 기본 구조
1. @기호와 함께 사용
2.  함수 또는 메서드 위에 위치
- 특징
1. 코드 재사용성 향상 →코드의 일부분을 여러 함수에서 공유
2. 코드 가독성 향상 → 코드 이해하기 쉬워짐
3. 관심사 분리 → 함수는 핵심 기능에만 집중할 수 있음
- 데코레이터 예제
1. 타이머 데코레이터 : @timer_decorator
2. 로깅 데코레이터 : @logging_decorator
- 인자가 있는 데코레이터 예제
1. 함수 호출 제한 데코레이터 : @limit_calls_decorator(n)
2. 권한 확인 데코레이터 : @permission_required_decorator(’문자열’)

```python
def my_decorator(func):
	def wrapper():
		print("데코레이터가 추가한 내용")
		func()
		print("데코레이터가 추가한 내용")
	return wrapper

def hello():
	print("안녕하세요")
	
decorated_hello = my_decorator(hello)
decorated_hello()

#@기호를 이용하면 간단하고 직관적이게 코드 작성 가능, 동일한 효과
def my_decorator(func):
	def wrapper():
		print("데코레이터가 추가한 내용")
		func()
		print("데코레이터가 추가한 내용")
	return wrapper
	
@my_decorator
def hello():
	print("안녕하세요")

hello()
```

[https://ctkim.tistory.com/entry/데코레이터decorator#google_vignette](https://ctkim.tistory.com/entry/%EB%8D%B0%EC%BD%94%EB%A0%88%EC%9D%B4%ED%84%B0decorator#google_vignette)