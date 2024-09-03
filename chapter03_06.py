# Chapter03_06
# 집합(Set) 특징
# 집합(Set) 자료형(순서X, 중복X)

# 선언
a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6])
d = set([1, 2, 'Pen', 'Cap', 'Plate'])
e = {'foo', 'bar', 'baz', 'foo', 'qux'}
f = {42, 'foo', (1, 2, 3), 3.14159}
# 기본적으로 set은 리스트형태로 묶지만 {}사용할수도 있다

print('a-', type(a), a) # 리스트에 중복된 값이 있어도 하나만 출력됨
print('b-', type(b), b)
print('c-', type(c), c)
print('d-', type(d), d)
print('e-', type(e), e)
print('f-', type(f), f)

# 튜플 변환(set -> tuple)
t = tuple(b)
print('t-', type(t), t)
print('t-', t[0], t[1:3])

# 리스트 변환 (set -> list)
l = list(c)
l2 = list(e)

print('l-' , l)
print('l2-' , l2)

# 길이
print(len(a))
print(len(b))
print(len(c))
print(len(d))
print(len(e))
print(len(f))


# 집합 자료형 활용
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7 ,8, 9])

print('s1 & s2', s1 & s2) #교집합
print('s1 & s2', s1.intersection(s2))

print('s1 | s2', s1 | s2) #합집합
print('s1 | s2', s1.union(s2))

print('s1 - s2', s1 - s2) #차집합
print('s1 - s2', s1.difference(s2))

# 중복 원소 확인
print('s1 & s2', s1.isdisjoint(s2))
# 중복원소가 있으면 False 없으면 True임

# 부분 집합 확인
print('Subset', s1.issubset(s2))  # s1이 s2에 부분집합인가? 맞으면 True, 틀리면 False
print('Superset', s1.issuperset(s2))

# 추가 & 제거
s1  = set([1, 2, 3, 4])
s1.add(5)
print('s1-', s1)

s1.remove(2)
print('s1-', s1)

s1.discard(7) 
print('s1-', s1)
# remove로 없는 원소를 제거할때는 에러가 발생하지만 discard로 삭제하면 에러발생이 없음

s1.clear()
print('s1-', s1)
# clear를 사용하면 전부 다 삭제됨

