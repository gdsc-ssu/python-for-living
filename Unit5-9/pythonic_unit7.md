### 1. 장식적인 출력 포매팅

```python
f'Results of the {year} {event}'

'{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)
print('{0} and {1}'.format('spam', 'eggs'))
print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; ''Dcab: {0[Dcab]:d}'.format(table))
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))

print('The value of pi is approximately %5.3f.' % math.pi)
```

- 포맷 문자열 리터럴 : f 또는 F 를 붙여 문자열 시작, 문자열 안에서 {} 안에 변수 또는 리터럴 값을 참조할 수 있는 파이썬 표현식 작성 가능
    - 변수 뒤에 :정수 를 전달하면 해당 필드 최소 문자 폭
    - {} 속 변수에 수정자를 추가하면 포맷 전 값 변환 가능
    - !a : ascii() / !s : str() / !r : repr()
    - {변수=} : 변수 = 변수 값
- 문자열의 str.format() 메서드는 변수 대체 위치에 {}를 사용하고 자세한 포매팅 디렉티브 제공 가능, 포맷할 정보도 제공
    - 위치와 키워드 인자를 자유롭게 조합할 수 있음
    - [ ]를 통해 딕셔너리 키를 액세스할 수 있음
    - ** 표기법을 사용해 딕셔너리 인자 전달 가능
- %연산

```python
s = 'Hello, world.'

str(s) # Hello, world.
repr(s) # 'Hello, world.'
# 숫자, 리스트, 딕셔너리는 보통 동일

s = 'Hello, world.\n'
str(s) # 줄바꿈 적용
repr(s) # 'Hello, world.\n'
```

- 수동 문자열 포매팅
    - str.rjust(x) : 우측 줄에 맞춤
    - str.ljust(x)
    - str.center(x)
    - str.zfill(x) : 숫자 문자열 왼쪽에 0을 채움

### 2. 파일 읽고 쓰기

```python
f = open(filename, mode, encoding=None)
```

- mode
    - r : 읽기
    - w : 쓰기
    - a : 파일 덧붙이기
    - r+ : 읽고 쓰기
    - b를 추가 : 바이너리 모드, 데이터는 바이트 객체의 형태로 읽고 씀

```python
with open('workfile', encoding="utf-8") as f:
    read_data = f.read()

# 파일이 자동으로 닫혔는지 확인할 수 있습니다.
f.closed
```

- with 키워드를 사용하지 않으면 f.close() 를 호출해서 파일을 닫고 사용된 시스템 자원을 즉시 반납해야함
- 파일 객체가 닫힌 후에는 wiht문이나 f.close() 를 호추하는 경우 모두, 파일 객체를 사용하려는 시도는 자동 실패

- f.read(size) : size가 없거나 음수면 내용 전체를 읽어서 돌려줌.
- f.readline() 은 파일에서 한 줄을 읽음. 개행문자 보존
- list(f) or f.readlines() : 모든 줄을 리스트로 읽어들임
- f.write(string) : string 내용을 파일에 쓰고 출력된 문자들의개수 돌려줌
- f.tell() : 파일의 현재 위치를 가리키는 정수 돌려줌
- f.seek(offset, whence) : 파일 객체의 위치 바꾸기. 기준점(whence)에서 offset을 더해서 계산. whence 기본값은 0

- json이라는 표준 모듈은 파이썬 데이터 계층을 받아서 문자열 표현으로 바꿔줌 ⇒ 직렬화
- 문자열 표현으로부터 데이터를 재구성 하는 것 ⇒ 역 직렬화

```python
import json
x = [1, 'simple', 'list']
json.dumps(x) # '[1, "simple", "list"]'
```

- dump() 라는 dumps() 함수의 변종, 객체를 텍스트 파일로 직렬화.