### 1. 문법 에러(파싱 에러)

- Syntax Error

### 2. 예외

- 실행 중 감지되는 에러들을 예외라고 부름
- 예외는 프로그램이 처리하지 않아서, 에러 메시지를 만듦
- 예) ZeroDivisionError, NameError, TypeError (내장 예외들)

### 3. 예외 처리하기

- 선택한 예외를 처리하는 프로그램 만들기

```python
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError: # ValueError 에러가 오면 실행
        print("Oops!  That was no valid number.  Try again...")
    except (RuntimeError, TypeError, NameError): # 튜플로 여러 개의 에외 지정 가능
		    pass
```

- 각기 다른 예외에대한 처리기 지정을 위해 try 문은 하나 이상의 except 절을 가질 수 있음

```python
class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
```

- except 절에 있는 클래스는 해당 클래스 자체나자식 클래스의 인스턴스인 예외와 매치됨

```python
try:
    raise Exception('spam', 'eggs')
except Exception as inst: # 예외를 inst 로 받는다
    print(type(inst))    # 예외
    print(inst.args)     # .args 에 저장된 인자들
    print(inst)          # __str__ 는 args 가 직접 인쇄될 수 있게합니다,
                         # 하지만 예외 서브 클래스가 재정의할 수 있습니다
    x, y = inst.args     # args 를 언팩합니다
    print('x =', x)
    print('y =', y)
```

→ inst = Exception(’spam’,’eggs’) 이 객체를 받는 것과 같음

Exception 객체
├─ args = ("spam", "eggs")
├─ __str__()
└─ __repr__()

- 예외 클래스 계층 구조

BaseException
├─ Exception        ← 우리가 일반적으로 다루는 예외
├─ SystemExit
├─ KeyboardInterrupt
└─ GeneratorExit

- BaseException에는 다양한 에러들이 포함되어 일반 예외만 잡기위해 Exception 을 잡아야함.
- 아래 코드가 가장 좋은 예외 처리 패턴

```python
try:
    something()
except Exception as e:
    print("Error:", e)
    raise
```

- try … except 문은 선택적인 else 절을 가짐. 있다면 모든 except 절 뒤에 와야 함. try절이 예외를 일으키지 않을때만 실행될 때 유용
- 예외 처리기는 try 절에서 호출되는 내부 함수들에서 발생하는 예외들도 처리

### 4. 예외 일으키기

- rasie 문 사용
- raise 에 제공하는 단일 인자는 발생시킬 예외,

### 5. 예외 연쇄

```python
try:
    open("database.sqlite")
except OSError:
    raise RuntimeError("unable to handle error")
```

→ open() 실패 → FileNotFoundError 발생 (OSError의 자식) → except OSError: 실행 → 그 안에서 새로운 예외 발생

- 첫 번째 예외를 처리하는 도중 두 번째 예외가 발생함 == 암묵적 예외 체이닝 - During handling….
- 명시적 예외 체이닝 - direct cause
- rasie…from 을 쓰면 원인 관계를 명확히 지정 가능

- 예외 변환 : 낮은 레벨 예외 → 의미 있는 높은 레벨 예외

```python
def func():
    raise ConnectionError

try:
    func()
except ConnectionError as exc:
    raise RuntimeError('Failed to open database') from exc
```

→ ConnectionError 발생 → except 에서 잡음 → RuntimeError로 변환 → from exc로 원인 해결

- raise —- from Nome : 기존 예외를 숨김. 체이닝 제거

- 기본체이닝 : __context__에 이전 예외 저장
- raise … from exc : __cause__에 이전 예외 저장
- raise … from Nome : __suppress_context__ = True

### 6. 사용자 정의 예외

- 새 예외 클래스를만들어서 자신의 예외에 이름 붙일 수 있음

### 7. 뒷정리 동작 정의

- try 는 finally 절이있으면 try 문이 완료되기 전에 finally 절이 마지막 작업으로 실행됨. try 문이 예외 생성하는지와 관계 없이 실행되는 문장임
- 예외 발생 시 finally 실행 후 예외 다시 발생

### 8. 미리 정의된 뒷정리 동작들

```python
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
```

- for 문이 아닌 with 문을 사용함으로써 문장이 실행된 후에, 줄을 처리하는 문제가 발생하더라도 파일 f 는 항상 닫힘.

 

### 9. 여러 개의 서로 관련 없는 예외를 동시 처리

- 첫 번째 예외 발생으로 바로 종료 하면 안되니까
- 동시성 상황 : 여러 개의 비동기 작업, 실패한 경우 모두 보고
- 검증 상황 : 하나 고치고 다시 실행 보단 모든 오류 한 번에 보고
- ExceptionGroup이 존재.

```python
except* OSError as e:
# 그룹 전체 중 OSError만 분리해서 꺼낸 뒤 처리

ExceptionGroup("errors", [ValueError, TypeError]) # X
ExceptionGroup("errors", [ValueError(), TypeError()]) # O
```

- ExceptionGroup 안에는 예외 타입이 아닌 이미 발생한 예외 인스턴스가 들어가야함!
- 예외 타입에는 정보가 안 들어있기 때문에..

### 10. 예외에 추가 정보 덧붙이기

```python
raise TypeError("bad type") # 이런 식으로 메시지를 고정

try:
    raise TypeError("bad type")
except Exception as e:
    e.add_note("Add some information")
    e.add_note("Add some more information")
    raise
    
# 출력
TypeError: bad type
Add some information
Add some more information
```

- add_note() 를사용해 기존 traceback 유지하며 추가 가능
- 새 예외를 raise 하면 traceback 손실, 원래 예외 타입 손실, 체이닝 복잡 등의 문제로 위 방법이 나음