# Chapter06_1
# 파이썬 클래스
# OOP(객체 지향 프로그래밍), Self, 인스턴스 메소드, 인스턴스 변수

# 클래스 and 인스턴스 차이 이해
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 접근 가능, 공유
# 인스턴스 변수 : 객체마다 별도 존재
# 클래스는 붕어빵 기계라고 생각하고 인스턴스는 붕어빵 틀이라고 생각하면 됨

# 예제1
class Dog1: # object 상속
    # 클래스 속성
    species = 'firstdog'

    # 초기화/인스턴스 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 클래스 정보
print(Dog1)

# 인스턴스화
a = Dog1("Mikky", 2)
b = Dog1("baby", 3)

# 비교
print(a == b, id(a), id(b))

# 네임스페이스
print('dog1', a.__dict__)
print('dog1', b.__dict__)

# 인스턴스 속성
print('{} is {} and {} is {}'.format(a.name, a.age, b.name, b.age))

if a.species == 'firstdog':
    print('{0} is a {1}'.format(a.name, a.species))

print(Dog1.species)
print(a.species)
print(b.species)

# 예제2
# self의 이해 
class SelfTest:
    def func1():
        print('Func1 called')
    def func2(self):
        print(id(self))
        print('Func2 called')

f = SelfTest()

print(id(f))

#f.func1() # 에러발생
SelfTest.func1() # self 즉, 매개변수가 없을때는 클래스를 통해서 호출해야함
SelfTest.func2(f) # 출력됨
#SelfTest.func2() # 에러발생 매개변수가 필요한데 없기때문임
f.func2() # 출력됨 # self는 인스턴스를 요구함

# 예제3
# 클래스  변수, 인스턴스 변수
class warehouse:
    # 클래스 변수
    stock_num = 0 # 재고

    def __init__(self, name):
        # 인스턴스 변수
        self.name = name
        warehouse.stock_num += 1

    def __del__(self):
        warehouse.stock_num -= 1

user1 = warehouse('Lee')
user2 = warehouse('Cho')

print(warehouse.stock_num)

print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print('Before', warehouse.__dict__)
print('>>>>>', user1.stock_num)

del user1
print('after', warehouse.__dict__)

# 예제4
class Dog: # object 상속
    # 클래스 속성
    species = 'firstdog'

    # 초기화/인스턴스 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return '{} is {} years old'.format(self.name, self.age)

    def speak(self, sound):
        return '{} says {}!'.format(self.name, sound)


# 인스턴스 생성
c = Dog('july', 4)
d = Dog('Marry', 10)
# 메소드 호출
print(c.info())
print(d.info())
# 메소드 호출
print(c.speak('Wal Wal'))
print(d.speak('Mung Mung'))


