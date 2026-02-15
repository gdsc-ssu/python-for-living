## 데코레이터(Decorator)
> 어떤 함수를 인자로 받아 꾸며준 후 다시 함수로 리턴하는 함수
> 함수 내부에 변화 주지 않고 로직을 추가하고 싶을 때 사용
**데코레이터는 꾸며주는 함수 내부에 직접적 수정이나 로직 변환 불가** 

```python
def hello():
    print("안녕!")

def decorator(func):
    def wrapper():
        print("함수 실행 전")
        func()
        print("함수 실행 후")
    return wrapper

decorated = decorator(hello)
decorated()

# 함수 실행 전
# 안녕!
# 함수 실행 후
```
어떤 함수를 데코레이터로 꾸며주려면 그 함수의 선언부 위에 @데코레이터명을 적어주면 됨
@ 문법으로 더 깔끔하게

```python
def decorator(func):
    def wrapper():
        print("시작")
        func()
        print("끝")
    return wrapper

@decorator
def greet():
    print("안녕 파이썬!")

greet()

# 시작
# 안녕 파이썬!
# 끝ㅁ
```

예시 추가
```python
def say_hello():
    print("Hello")

def decorator(func):                        
    def sentence(*args, **kwargs):         
        print("Nice to meet you")      
        return func(*args, **kwargs)

    return sentence

@decorator
def say_hello():
    print("Hello")

say_hello()

# 실행 결과
Nice to meet you
Hello
```

데코레이터 동작 파악
```python
def decorator(func):                        #1
    def sentence(*args, **kwargs):          #3
        print("Nice to meet you")           #6
        return func(*args, **kwargs)        #7

    return sentence                         #4

@decorator                                  #3
def say_hello():                            #2
    print("Hello")                          #8


say_hello()                                 #5
```
#1 decorator 함수를 선언
#2 say_hello 함수 선언
#3 say_hello 함수를 decorator 함수로 꾸며줌. 이는 variable = decorator(say_hello)와 동일함. 따라서 sentence 함수도 이때 선언
#4 decorator 함수로 꾸며주었기에 say_hello 함수는 sentence 함수의 로직을 실행
#5 say_hello 함수 실행
#6 say_hello 함수는 sentence 함수의 로직을 가지고 있기 때문에 sentence 함수의 로직 실행
#7 decorator로 꾸며준 함수인 say_hello 함수를 호출하여 리턴
#8 호출된 say_hello 함수가 실행

class와 함께 사용도 가능
```python
class Decorator:
    def __init__(self, func):  # 꾸며줄 함수를 매개변수로 전달
        self.func = func       # 꾸며줄 함수를 속성에 저장

    def __call__(self, *args, **kwargs):
        print("Nice to meet you")
        self.func()            #속성에 저장된 함수 호출
        print(f"My name is {args[0]}")


@Decorator
def say_hello():
    print("Hello")


say_hello("Fox")

#실행 결과
Nice to meet you
Hello
My name is Fox
```

- 코드의 중복을 최소화하고 재사용성을 높일 수 있음
- 가독성 높일 수 있음. 로직 수정이 필요할 때도 데코레이터만 수정하면 됨
- **중첩해서 사용하면 디버깅 난이도 상승**

참고문서
https://tibetsandfox.tistory.com/10
