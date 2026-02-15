### 1. if 문

여러 개의 elif 문 가능, 들여쓰기로 구분함.

```python
x=int(input("정수 하나 입력 : "))

if x>0:
		print("Positive")
elif x==0:
		print("0")
else:
		x=0
		print("Negative")
```
객체 내 요소의 존재 존재 여부로 True, False

in, not in 으로 객체 내 특정 요소 존재 여부로 True, False

→ 여기서 객체는 일반적으로 리스트, 문자열, 튜플, 딕셔너리


### 2. for 문

반복 가능한 자료형 (리스트, 문자열)의 항목을 순서대로 이터레이트

```python
words = ['cat','dog','bird']

for w in words:
		print(w,end=' ')

# cat dog bird
```

컬렉션을 이터레이트 하는 동안 같은 컬렉션 수정 코드를 만들기도 함. 

```python
users={'Hans':'active','Eleo':'inactive','dong':'active'}

# inactive 삭제하기
for user, status in users.copy().items():
		if status == 'inactive'
				del users[user]
**#copy() 를 쓰는 이유는 반복 중 원본 자료를 변경하지 않기 위함.**

# active 컬렉션 새로 만들기
active_users={}
for user, status in users.item():
		if status == 'active'
				active_users[user]=status
```
리스트 내포 가능, if 조건문 추가 가능

```python
c = 'abcde'
a = [val + '' for val in c]
# ['ak','bk','ck','dk','ek']

b = [val+'k' for val in c if val == 'c']
# ['ck']
```


### 3. range 함수

수열을 만드는 함수 range(a,b,c) ⇒ a≤x<b  c : 증가분

```python
for i in range(1,6)
		print(i,end=' ')
		
# 1 2 3 4 5

list(range(1,10,2))
#[1, 3, 5, 7, 9]

# 음수도 가능
list(range(-10,-100,-30))
#[-10, -40, -70]
```

```python
a=['aa','bb','cc']
for i in range(len(a)):  # len(a) = 3
		print(i, a[i])
# range(3) == range(0,3)
		
**# enumerate() 가 좀 더 유용**
for i,l in enumerate(a):
		print(i,l)

#0 aa
#1 bb
#2 cc
```

range 가 돌려준 객체는 리스트가 아님! 

→ 이터러블(iterable) 객체를 돌려줌. 이는 멤버들을 한 번에 하나씩 돌려줄 수 있는 객체.
내림차순으로 가고싶은 경우

```python
for i in range(7,0-1,-1):
		print (i,end=' ')
# 7 6 5 4 3 2 1 0
```


### 4. break와 continue 문

break : 루프를 빠져나감

continue : 루프의 다음 이터레이션에서 계속하도록 넘어감


### 5. 루프의 else 절

if 문의 else가 아니라 루프의 else (try 의 else와 유사)

```python
for n in range(2,10):
		for x in range(2,n):
				if n%x==0:
						print(n,'equals',x,'*',n//x)
						break
		**else**: **# 루프에서 예외처리한 것**
				print(n,"is a prime number")
```
→ 반복문과 else 를 같이 사용하면 else 부분을 마지막에 반드시 실행함. 위 코드에서 break 가 존재하는 이유.

try의 else 문은 사용이 다르다 (try-except-else-finally)

try - 실행하려는 구문

except - 있어야 else 사용 가능, 에러 발생시 실행

else - 에러 발생하지 않을 시 실행

finally - 반드시 실행


### 6. pass 문

아무것도 하지 않고 넘어감.

```python
while True:
		pass
```

최소한의 클래스를 만들 때, 함수나 조건부 바디 채울 때 주로 사용함.

```python
class MyClass:
		pass
		
def function(*args):
		pass
		
**# 문법적으로 자리는 필요한 데 실행할 코드가 없을 때**
```

참고 자료
https://easyjwork.tistory.com/9
https://easyjwork.tistory.com/10
https://devpouch.tistory.com/70
https://miny-genie.tistory.com/179

