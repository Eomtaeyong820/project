#기본출력
print('start python!')

#separator 옵션
print('p', 'y', 't', 'h', 'o', 'n', sep='')
print('010', '6543', '8805', sep='-')
print('xodyd820', 'naver.com', sep='@')

#end 옵션
print('Welcome to', end='  ')
print('IT news', end='')
print('Web site')

#file 옵션
import sys #import는 예약어임.
print('Learn python', file=sys.stdout) #해당 파일에 Learn python이라는 문자를 추가하고 적고싶을때 사용함 

#format 사용(d='정수',s='문자열',f='실수')
print('%s %s' % ('one', 'two'))
print('{},{}'.format('one','two'))
print('{1},{0}'.format('one','two'))

name='태용'
print('my name is {}'.format(name))

name='태용'
age=23
print('my name is {} and i am {}years old'.format(name,age))

# %s의 사용
print('%10s'%('nice')) #여기서 %10s의 10은 10개의 자릿수를 의미함 출력은 오른쪽에서부터 출력
print('{:>10}'.format('nice')) #format함수를 사용해서 똑같이 표현할수있다 오른쪽에서부터 출력

print('%-10s'%('nice')) #10앞에 -를 붙이게되면 왼쪽에서부터 문자열이 출력됨 
print('{:10}'.format('nice')) # '>'이 기호를 제거하면 왼쪽에서부터 문자열이 출력됨

print('{:_>10}'.format('nice')) # '_>'이 기호 사용시 nice를 제외한 왼쪽 6자릿수가 _로 대체됨
print('{:^10}'.format('nice')) # '^'이 기호 사용시 nice문자열이 가운데 정렬함

print('%.5s' % ('nice')) #5번째 자릿수까만 출력됨
print('%.5s' % ('python')) #그래서 pytho까지만 출력
print('{:10.5}'.format('python')) #공간은 10개를 확보하나 5개만 출력하게 됨

# %d의 사용
print('%d %d' % (1,2)) #정수 1과 2 출력
print('{} {}'.format(1,2)) #정수 1과 2 출력

print('%4d' % (42)) #정수 4자릿수 중에 오른쪽에서 부터42를 출력
print('{:4d}'.format(42)) #정수 4자릿수 중에 오른쪽에서 부터 42를 출력

# %f의 사용
print('%f' % (3.141592)) #실수 3.141592를 출력
print('{:f}'.format(3.141592)) #실수 3.141592를 출력

print('%06.2f'% (3.141592)) 
# %06.2의 의미는 6은 6개의 자릿수를 의미하고 2는 소수점아래 두 자릿수를 출력함, 0은 나머지 공백을 채우는 숫자임
#즉 3 앞에 00 2개 가 붙고 소수점아래  2자리의인 14가 출력 즉 -> 003.14가 출력됨
print('{:06.2f}'.format(3.141592)) # 위의 코드와 같이 003.14가 출력됨

#format함수 정리
# s의 경우 -> print('{:10}'.format('nice')) -> {}안에 s가 삽입되지 않아야 함
# d의 경우 -> print('{:4d}'.format(42)) -> {}안에 d가 삽입되어야 함
# f의 경우 -> print('{:f}'.format(3.141592)) -> {}안에 f가 삽입되어야 함

