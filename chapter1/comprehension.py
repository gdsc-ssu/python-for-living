##################################################
# 리스트
# 기본
# numbers = []
# for i in range(5):
#     numbers.append(i)
# 리스트 컴프리헨션 사용
numbers = [i for i in range(5)]
print('numbers :',numbers)

# 고급(중첩 루프)
# pairs = []
# for x in range(3):
#     for y in range(3):
#         pairs.append((x,y))
pairs = [(x, y) for x in range(3) for y in range(3)]
print('pairs :',pairs)

# 고급(조건 및 중첩 루프)
# not_same_pairs = []
# for x in range(3):
#     for y in range(3):
#         if x != y:
#             not_same_pairs.append((x, y))
not_same_pairs = [(x, y) for x in range(3) for y in range(3) if x != y]
print('not_same_pairs :', not_same_pairs)

# 문자열
# words = ['java', 'python', 'dart']
# upper_words = []
# for word in words:
#     upper_words.append(word.upper())
words = ['java', 'python', 'dart']
upper_words = [word.upper() for word in words]
print('upper_words :',upper_words)

##################################################
# 딕셔너리
dic_numbers = {i : i for i in range(5)}
print(dic_numbers)
##################################################
##################################################
# 집합
data = [1, 2, 2, 3, 4, 4]
set_numbers = {i for i in data}
print(set_numbers)
##################################################
# 제너레이터
generator_numbers = {i for i in data}
print(list(generator_numbers))
##################################################