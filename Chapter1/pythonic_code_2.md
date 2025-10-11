- 언패킹과 제너레이터

**언패킹**

: 묶여 있는 객체를 여러 개의 값으로 풀어주는 개념

- 기본 구조
1. 가변인자를 언패킹하는 경우 , *
2. 키워드인자를 언패킹하는 경우, **

→ 매개변수에서 * 을 붙이는 게 아니라 인자 앞에 *을 붙여서 사용

```python
#가변인자 언패킹
def sum(a,b,c):
	return a+b+c

numbers=[1,2,3]
print(sum(*numbers))
```

```python
#키워드인자 언패킹
def cal(first,op,second):
	if op=='+':
		return first+second
	if op=='-':
		return first-second
	if op=='*':
		return first*second
	if op=='/':
		return first/second
obj={
'first' : 11,
'second' : 33,
'op' : '*'
}

cal(**obj)
```

https://ground90.tistory.com/131

**제너레이터**

: iterator를 생성해 주는 함수, 일반함수와 차이는 generator함수가 실행 중 yield를 만날 경우, 해당 함수는 그 상태로 정지 되며 반환값을 next()를 호출한 쪽으로 전달하게 됨. 종료되는 것이 아니라 그 상태로 유지

→ 함수 내부에서 사용된 데이터들이 메모리에 유지

**yield : 해당 키워드 라인을 실행하고 함수를 호출한 쪽으로 프로그램의 제어를 넘겨줌

- 특징
1. 메모리를 효율적으로 사용

→ 데이터의 값을 한꺼번에 메모리에 적제하는 것이 아니라 next() 메소드를 통해 차례로 값에 접근할 떄마다 메모리에 적재하는 방식

1. 계산 결과 값이 필요할 때까지 계산을 늦추는 효과

```python
def generator(n):
	i=0
	while i<n:
		yield i
		i+=1
for x in generator(5):
	print(x)
	
'''
실행 중 while 문 안에서 yield 만남 
-> return 과 비슷하게 함수를 호출했던 구문으로 반환 
-> 첫번재 i 값인 0 을 반환하게 된다. 
-> 반환 하였다고 generator 함수가 종료되는 것이 아니라 그대로 유지한 상태이다.
-> x 값에는 yield 에서 전달 된 0 값이 저장된 후 print 
-> for 문에 의해 다시 generator 함수가 호출
-> generator 함수가 처음부터 시작되는게 아니라 yield 이후 구문부터 시작 
-> i += 1 구문이 실행되고 i 값은 1로 증가.
-> while 문 내부이기 때문에 yield 구문을 만나 i 값인 1이 전달
-> x 값은 1을 전달 받고 print
'''
```

https://bluese05.tistory.com/56