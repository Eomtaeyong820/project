# Chapter05_0
# 함수란? 완전 함수 기초 설명
# 파이썬 함수 쌩기초

# 함수
# 프로그래머가 이름을 통해서 정의 후 필요할 때 마다 호출
# 반복 되는 코드를 한 번 구현 후 재사용 가능한 코드의 집합
# 함수 구현 -> 재사용, 루틴(프로시저, 서브루틴)

# 종류
# 1. 매개변수가 필요한 함수
# 2. 매개변수가 필요없는 함수
# 3. 결과값을 반환하는 함수(return)
# 4. 결과값을 반환하지 않는 함수

# 예제1 : 매개변수 필요X
def funtion1():
    print('예제1 호출')

# 예제2 : 매개변수 필요O
def funtion2(a, b):
    print('예제2 호출', a, b)

# 예제3 : 결과값 반환 X
def funtion3(x, y):
    print('예제3 호출', x, y)

# 예제4 : 결과값 반환O
def funtion4(x, y):
    return x * y


# 실행
funtion1()
funtion2(10, 20)
funtion3(100, 200)
funtion4(50, 50)

r = funtion4(50,50)

print('예제4 호출', r)