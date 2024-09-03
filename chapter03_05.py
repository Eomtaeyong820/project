# Chapter 03_05
# 파이썬 딕셔너리
# 범용적으로 가장 많이 사용
# 딕셔너리 자료형(순서X, 키중복X, 수정O, 삭제O)

# 선언 
# {}를 사용하며, {'Key': 'Value'}로 이루어져 있음
# Key는 어떤 자료형도 가능함

a = {'name': 'Kim', 'Phone': '01065438805', 'Birth': '020820'}
b = {0: 'Hello python'}
c = {'arr': [1, 2, 3, 4]}
d = {
    'name': 'niceman',
    'city': 'ulsan',
    'age': 23,
    'grade': 'A',
    'status': True
}
e = dict([
    ('name', 'niceman'),
    ('city', 'ulsan'),
    ('age', 23),
    ('grade', 'A'),
    ('status', True)
])
# dict을 사용해서 리스트로 묶고 튜플로 나타내서 사용하는데 불편하긴하나 정석임

f = dict(
    name='niceman',
    city='ulsan',
    age=23,
    grade='A',
    status=True
)
#주로 f의 방식으로 많이 사용함

print('a-', type(a), a)
print('b-', type(b), b)
print('c-', type(c), c)
print('d-', type(d), d)
print('e-', type(e), e)
print('f-', type(f), f)

# 출력
print('a-', a['name']) # 존재X -> 오류발생
print('a-',a.get('name')) # 존재O -> None 처리
print('b-', b[0])
print('b-',b.get(0))
print('f-',f.get('city'))
print('f-',f.get('age'))

# 딕셔너리 추가
a['address'] = 'seoul'
print('a-', a) # 변수 a에 key값 address와 value값 seoul이 추가됨
a['rank'] = [1, 2, 3]
print('a-', a) # 리스트도 추가됨

# 딕셔너리 길이
print('a-', len(a)) # KEY의갯수를 알려줌
print('b-', len(b))
print('c-', len(c))
print('d-', len(d))

# dict_keys, dict_values, dict_items : 반복문(_iter_)에서 사용가능
print('a-', a.keys())
print('b-', b.keys())
print('c-', c.keys()) # KEY값들만 뽑아서 가져옴
print('a-', list(a.keys()))
print('b-', list(b.keys())) # KEY값들을 리스트 형태로 출력

print('a-', a.values())
print('b-', b.values())
print('c-', c.values()) # value값들만 뽑아서 가져옴
print('a-', list(a.values()))
print('b-', list(b.values())) # value값들을 리스트 형태로 출력

print('a-', a.items())
print('b-', b.items())
print('c-', c.items()) # key와 value가 한 쌍으로 이루어져서 출력됨
print('a-', list(a.items()))
print('b-', list(b.items())) 

# POP Method
print('a-', a.pop('name'))
print('a-', a) # name키와 value 꺼내져서 삭제됨
print('c-', c.pop('arr'))
print('c-', c)

print('a-', a.popitem())
print('a-', a) # 무작위로 key와 value값을 꺼내서 삭제함

# in Method 
# Key가 있는지 조회가 가능함

print('a-', 'Birth' in a) # a에 Birth라는 키가 있으면 True 없으면 False출력
print('a-', 'city' in d) # 참고) 대소문자 구별해줘야함

# 수정
a['address'] = 'test_dict'
print('a-', a)

a['address'] = 'EOM'
print('a-', a)

# 문법적으로 확실히 할거면 update 사용

a.update(Birth= '020418')
print('a-', a)

temp = {'address': 'Busan'}
a.update(temp)
print('a-', a) # 명시적으로 나타낼수도 있음

