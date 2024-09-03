# Chapter 06-2
# 파이썬 모듈
# Moudule : 함수, 변수, 클래스 등 파이썬 구성 요소 등을 모아놓은 파일

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def power(x, y):
    return x ** y

# print('-' * 15)
# print('called inner!')
# print(add(5,5))
# print(subtract(15,5))
# print(multiply(5,5))
# print(divide(10,2))
# print(power(5,3))
# print('-' * 15)

# __name__ 사용
# <- 이 코드는 다른 사용자가 import 함수를 사용하여 모듈로 사용할려고 할때
# __main__이라는 예약어를 사용하면 내 파일에서 실행되지만 상대방이 내 파일을 module로 쓸려고 할 때는 출력X

if __name__ == "__main__":
    print('-' * 15)
    print('called inner!')
    print(add(5,5))
    print(subtract(15,5))
    print(multiply(5,5))
    print(divide(10,2))
    print(power(5,3))
    print('-' * 15) 

