# Chapter 03_2
# 파이썬 문자형
# 문자형 중요

# 문자열 생성
str1 = 'i am Python'
str2 = 'Python'
str3 = 'How are you?'
str4 = 'Thank you!'

print(len(str1), len(str2), len(str3), len(str4))
# len은 문자열의 길이를 알려준다(공백을 포함함)

# 빈 문자열
str1_t1 = ''
str2_t2 = str()

print(type(str1_t1),len(str1_t1))
print(type(str2_t2),len(str2_t2))

# 이스케이프 문자 사용

# \n : 개행(줄바꿈) \t: 탭만큼 문자이동 \\: 문자 \': 문자
# \000 : 널 문자

print('I\'m boy') # \(역슬러쉬를 사용하면 \뒤에 특수문자는 있는 그대로가 됨)
print('a \t b')
print('a \n b')

escape_str1 = "Do you have a \"retro games\"?"
print(escape_str1)

#탭, 줄 바꿈
t_s1 = "Click \t start!"
t_s2 = "New Line \n Check!"

print(t_s1)
print(t_s2)

#Raw string 
#Raw string은 역슬래쉬를 있는 그대로 표시할 수 있음(이스케이프 사용안할떄 사용)
#파일의 경로를 나타날떄 \ 많이 사용되기 때문에 알아두면 좋음

raw_s1 = r'D:\python\test'

print(raw_s1)

# 멀티라인 입력
# 역슬래시 사용

multi_str = \
'''
String
Multi line
Test
'''

print(multi_str)

# 문자열 연산
str_o1 = "Python"
str_o2 = "Apple"
str_o3 = "How are you doing?"
str_o4 = "Seoul Deajeon Busan Jinju"

print(str_o1 * 3) # Python 문자열이 3번 반복해서 출력됨
print(str_o1 + str_o2) # 문자열이 합쳐서 출력됨
print('y' in str_o1) # str_o1 변수에 y라는 문자가 있는지 출력됨(True 출력)
print('n' in str_o1) # True 출력
print('p' not in str_o2) # False 출력

#문자열 형 변환
print(str(66),type(str(66)))
print(str(10.1))
print(str(True), type(str(True)))

#문자열 함수(upper, isalnum, startswith, count...)

print("Capitalize:", str_o1.capitalize())
#첫 글자를 대문자로 바꿔줌
print("endswith:", str_o2.endswith("e"))
#마지막 글자가 e로 끝나는지 찾아줌 맞으면 TRUE 틀리면 false출력
print("replace:",str_o1.replace('thon', 'good'))
#thon이라는 문자열을 good이라는 문자열로 교체 후 출력함
print("sorted:", sorted(str_o2))
#문자열을 분류해서 출력함
print("split:",str_o4.split(' '))
#공백으로 구분된 단어들을 하나하나 리스트 형태로 구분해서 출력함
#Seoul Deajeon Busan Jinju 이렇게 출력됨

#반복(시퀀스)
im_str = 'Good boy!'

print(dir(im_str)) # _iter_가 클래스에 있으면 반복문 가능

#출력
for i in im_str:
    print(i) #슬라이싱 처리가 되서 출력됨

#슬라이싱
str_s1 = 'Nice Python'

#슬라이싱 연습
print(str_s1[0:3]) # 0~2번째 문자열 출력 [0:N]일때 N-1까지 출력으로 이해
print(str_s1[5:]) # 5번째부터 끝까지 출력
print(str_s1[:len(str_s1)]) # 문자열 전체를 출력할때 이런식으로 표현가능
print(str_s1[:len(str_s1)-1]) # '-'음수는 왼쪽에서 부터 오른쪽으로 출력
print(str_s1[1:9:2]) # 1번 부터 9번까지 2씩 건너띄며 출력
print(str_s1[-5:]) # -5번부터 끝까지 출력
print(str_s1[1:-2]) # 1번부터 -2까지 출력 
print(str_s1[::2]) # 처음부터 끝까지 2개씩 건너띄며 출력
print(str_s1[::-1]) # 반대로 출력됨

# 아스키 코드(또는 유니코드)
a = 'z'
print(ord(a)) # ord는 문자 -> 아스키코드
print(chr(122)) # chr은 아스키코드 -> 문자


