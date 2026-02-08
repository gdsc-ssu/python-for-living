# 4.2 for 문 예제

# 시퀀스 순회
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

print()

# 전략 1: 사본을 이터레이트하며 수정
users = {'alice': 'active', 'bob': 'inactive', 'charlie': 'active'}
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
print("전략 1 결과:", users)

# 전략 2: 새 컬렉션 만들기
users = {'alice': 'active', 'bob': 'inactive', 'charlie': 'active'}
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
print("전략 2 결과:", active_users)
