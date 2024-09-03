# Chapter 03_04
# 파이썬 튜플
# 리스트와 비교 중요
# 튜플 자료형(순서O, 중복O, 수정X, 삭제X) #불변

# 선언

a = ()
b = (1,) # 원소가 1개일 경우 끝에 ','를 붙어야 튜플로 인식
c = (11, 12, 13, 14)
d = (100, 1000, 'Ace', 'Base', 'Captine')
e = (100, 1000, ('Ace', 'Base', 'Captine'))

# 인덱싱
print('>>>>>')
print('d-', d[1])
print('d-', d[0] + d[1] + d[1])
print('d-', d[-1])
print('d-', e[-1])
print('d-', e[-1][1])
print('d-', list(e[-1][1])) # list함수를 사용하면 튜플을 리스트로 변경가능

# 수정X
#d[0] = 1500 (튜플은 수정이 안된다고 출력됨)

# 슬라이싱
print('>>>>>')
print('d-', d[0:3])
print('d-', d[2:])
print('d-', e[2][1:3])

# 튜플 연산
print('>>>>')
print('c + d', c + d)
print('c * 3', c * 3)

# 튜플 함수
a = (5, 2, 3, 1, 4)
print('a-', a)
print('a-', a.index(3))
print('a-', a.count(2))

# 팩킹 & 언팩킹(Packing, and Unpacking)

# 팩킹
t = ('foo', 'bar', 'baz', 'qux')

print(t)
print(t[0])
print(t[-1])

# 언패킹1
(x1, x2, x3, x4) = t # 4개의 원소가 각각 순서에 맞는 변수로 할당됨

print(type(x1), type(x2), type(x3), type(x4))
print(x1, x2, x3, x4)

# 팩킹 & 언패킹
t2 = 1, 2, 3 #팩킹
t3 = 4, #팩킹
x1, x2, x3 = t2 #언팩킹
x4, x5, x6 = 4, 5, 6 #언팩킹

print(t2)
print(t3)
print(t2)
print(x4 ,x5,x6)

