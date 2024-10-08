# Chapter04_3
# 파이썬 반복문
# While 실습

# while <expr>:
#    <statement(s)>

# 예제1

n = 5
while n > 0:
    n = n - 1
    print(n)

# 예제2
a = ['foo', 'bar', 'baz']

while a:
    print(a.pop())

# 예제3

n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print('Loop Ended.')

# 예제4

m = 5
while m > 0:
    m -= 1
    if m == 2:
        continue
    print(m)
print('Loop Ended.')

# 예제5
i = 1

while i <= 10:
    print('i:', i)
    if i == 6:
        break
    i += 1

# while - else 구문

# 예제6

n = 10
while n > 0:
    n -= 1
    print(n)
    if n == 5:
        break
else: 
    print('else out')

# 예제7
a  = ['foo', 'bar', 'baz', 'qux']
s  = 'qux'

i = 0

while i < len(a):
    if a[i] == s:
        break
    i += 1
else:
    print(s, 'not found in list')

# 무한반복
# whilie true:와 같은 형식으로 사용하면 무한반복 발생

# 예제8
a  = ['foo', 'bar', 'baz']

while True:
    if not a:
        break
    print(a.pop())