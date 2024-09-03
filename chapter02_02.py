#파이썬 변수

#기본선언
n=700

#출력
print(n) #n의 값이 출력
print(type(n)) #n의 type을 알려줌 -> 현재 int(정수형)

#동시 선언
x = y = z= 700 #동시 선언도 가능함
print(x, y, z)

#선언
var=700

#재선언
var= 'Change value'

#출력
print(var) 
#var이라는 변수는 Change value로 출력되고 기존에 선언되어 있던 700은 참조가 됨
#즉, Change value로 덮어쓰기가 된거라고 생각하면 편함.
print(type(var)) #재선언된 Change value의 type인 str(문자열)이 출력됨

#Object reference
# 변수 값 할당 상태
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔 출력

# 예1
print(300)
#int를 사용하지 않아도 프로그래 자체에서 300을 정수(int)로 인식해서 300을 출력하게 됨 
print(int(300))

# 예2
# n -> 777
n= 777

print(n,type(n))

m = n
# m -> 777 <- n

print(m, n)
print(type(m), type(n)) # m도 n이랑 같은 값과 type을 가짐

m=400

print(m, n)
print(type(m), type(n)) # m=400을 할당하면 m=n은 참조가 되서 출력은 400이 됨

# id(identity)확인: 객체의 고유값 확인

m = 800
n = 655

print(id(m)) # id는 객체의 고유값(고유번호를 나타냄)
print(id(n))
print(id(m) == id(n)) 
# 변수값이 다르기 때문에 id도 다름 -> False출력(직관적으로 변수값이 다르니 false로 생각하면 편함) 

# 같은 오브젝트 참조 
m = 800
n = 800

print(id(m))
print(id(n))
print(id(m) == id(n)) 
# 변수값이 같아 id도 같음 -> True출력
#(생각해야할 점은 파이썬 자체에서 같은 값에 굳이 다른 id를 주면 메모리가 낭비되기 때문에 같은 id를 사용)

# 다양한 변수 선언(Naming Sense를 확인 할 수 있음)

# 1. Camel Case : numberOFCollegeGraduates -> Method에 사용함
# -> 앞에 첫글자는 소문자로 시작하고 OF를 대문자로 하여 대문자 사용

# 2. Pascal Case : NumberOFCollegerGraduates -> Class에 사용함
# -> 앞에 첫글자를 대문자로 그 뒤는 Camel Case와 동일함

# 3.Snake Case : number_od_college_graduates -> Python에서 주로 사용
# -> 모든 문자를 소문자로 사용하고 _기호를 넣음

# 예약어는 변수명을 불가능함  -> 예약어는 파이썬 자체에서 제공하는 언어
# 예) for, def, if ..

