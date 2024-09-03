# Chapter03_1
# 숫자형

# 파이썬 지원 자료형

# int : 정수, float: 실수, complex: 복소수, bool: 불린
# str: 문자열(시퀀스), list: 리스트(시퀀스), tuple: 튜플(시퀀스)
# set: 집합, dict: 사전

# 데이터 타입
str1 =  "Python"
bool = True
str2 = 'Anaconda'
float_v = 10.0 # 10은 정수지만 10.0은 실수임(사람의 관점에서 이해X)
int_v = 7
list = [str1, str2]
dict = {
    "name: Maching Learning"  
    "Version: 2.0"
}
#여기서 Name과 Version처럼 앞에있는 단어들을 KEY라고 부른다
tuple = (7, 8, 9)
set= {7, 8, 9}

#데이터 타입 출력
print(type(str1))
print(type(bool))
print(type(str2))
print(type(float))
print(type(int))
print(type(list))
print(type(list))
print(type(dict))
print(type(tuple))
print(type(set))

#연산 실습
i1 = 4
i2 = 2
f1 = 1.3
f2 = 3.6

print('i1+i2 =', i1+i2)
print('f1+f2 =', f1+f2)

#형 변환 실습
a = 3.
b = 6
c = .7
d = 12.7

#타입 출력
print(type(a), type(b), type(c), type(d))

#형 변환
print(float(b))
print(int(c))
print(int(d))
print(int(True)) #True: 1 False:0
print(float(False)) 

#수치 연산 함수
print(abs(-7))

x, y = divmod(100, 8)
print(x,y) # x에는 몫, y에는 나머지가 출력됨
print(pow(5,3), 5**3) # 5의 3제곱을 나타내는 2가지 표현

# 외부 모듈 
import math 

print(math.ceil(5.1)) # x 이상의 수 중에서 가장 작은 정수
print(math.pi)


