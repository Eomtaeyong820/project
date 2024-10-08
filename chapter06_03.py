# Chapter 06-3
# 파이썬 패키지
# 패키지 작성 및 사용법
# 파이썬은 패키지로 분할 된 개별적인 모듈로 구성
# 상대경로:..(부모 디렉토리), .(현재 디렉토리) -> 모듈 내부에서만 사용
# __init__.py : Python 3.3 부터는 없어도 패키지로 인식 -> 단, 하위 호화을 위해 작성 추천
# 예제1
import sub.sub1.module1
import sub.sub2.module2

# 사용
sub.sub1.module1.mod1_test1()
sub.sub1.module1.mod1_test2()

sub.sub2.module2.mod2_test1()
sub.sub2.module2.mod2_test2()

print()
print()
print()

# 예제2 위에 꺼 보다 코드를 줄일 수 있음
from sub.sub1 import module1
from sub.sub2 import module2 as m2 
# alias는 module에 별명 즉 변수명을 줄수있음

module1.mod1_test1()
module1.mod1_test2()

m2.mod2_test1
m2.mod2_test2

print()
print()
print()

# 예제3 *는 모든 파일을 불러오는것인데 웬만하면 사용하지 않기
from sub.sub1 import *
from sub.sub2 import *

module1.mod1_test1()
module1.mod1_test2()

module2.mod2_test1()
module2.mod2_test2()

# 연습 
import sub.sub1.chapter06_02

print(sub.sub1.chapter06_02.add(1,2))

from sub.sub1 import chapter06_02 as v

print(v.add(4, 8))



