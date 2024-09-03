# Chapter03_3
# 파이썬 리스트
# 자료구조에서 중요
# 리스트 자료형(순서O, 중복O, 수정O, 삭제O)

# 선언
a = []
b = list()
c = [70, 75, 80,85] #Len
d = [1000, 10000, 'Ace', 'Base', 'Captine']
e = [1000, 10000, ['Ace', 'Base', 'Captine']]
f = [21.42, 'foobar', 3, 4, False, 3.14159]

# 인덱싱
print('>>>>>')
print('d-', type(d), d)
print('d-', d[1]) # 10000이 출력
print('d-', d[0] + d[1] + d[1]) # 연산도 가능함
print('d-', d[-1]) # Captine이 출력
print('e-', e[-1][1]) # Base가 출력
print('e-', list(e[-1][1])) # Base가 리스트 형태로 출력

# 슬라이싱
print('>>>>')
print('d-', d[0:3])
print('d-', d[2:])
print('e-', e[-1][1:3])

#리스트 연산 
# -> 리스트를 연산하면 리스트가 결과로 나옴
print('>>>>')
print('c + d', c + d)
print('c * 3', c * 3)
print("'TEST' + c[0]", 'TEST' + str(c[0])) # c[0]가 int형이기 때문에 str로 문자형을 변환 후 출력함

# 값 비교
print(c == c[:3] + c[3:]) # True출력
print(c)
print(c[:3] + c[3:])

# identity(id)
temp = c # 같은 identity를 가짐
print(temp, c)
print(temp)
print(c) 

# 리스트 수정, 삭제
print('>>>>')
c[0] = 4
print('c-', c)
c[1:2] = ['a', 'b', 'c'] # 원소범위로 지정하면 리스트 각각 출력됨 [['a', 'b', 'c']]로 출력시 리스트 형태로 출력

print('c-', c)
c[1] =['a', 'b', 'c'] # 원소번호로 지정하면 리스트의 형태로 출력됨
print('c-', c)
c[1:3] = []
print('c-', c)
del c[2] # 리스트 삭제할 때 사용
print('c-', c)

# 리스트 함수
a = [5, 2, 3, 1, 4]

print('a-', a)
a.append(10) # 리스트 맨끝에 원하는 값을 넣어줌
print('a-', a)
a.sort() # 리스트를 오름차순으로 정렬함
print('a-', a)
a.reverse() # 리스트를 역순으로 정렬(내림차순)
print('a-', a)
print('a-', a.index(3), a[3]) # 리스트를 찾는 방법 2가지 (index사용, []리스트 사용)
a.insert(2,7) #insert함수는 리스트 사이에 삽입가능(위치,추가할 값)
print('a-', a)
a.reverse()
print('a-', a)
a.remove(10) # 제거할 값을 넣으면 제거됨 
print('a-', a)
print('a-', a.pop()) 
# pop함수는 기존의 리스트에서 마지막에 해당하는 원소를 가져오고 나머지 원소들로 리스트 재구성
print('a-', a)
print('a-', a.pop()) 
print('a-', a)
print('a-', a.count(4)) # (X) X라는 값이 리스트안에 몇개가 있는지 알려주는 함수
ex = [8,9]
a.extend(ex)
print('ex-', ex)

# 삭제: remove, pop, del

# 반복문 활용
while a:
    data = a.pop()
    print(data)

