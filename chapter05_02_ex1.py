# Chapter05_2_ex1
# 파이썬 사용자 입력
# Input 사용법
# 기본 타입(str)

# 예제1 -> 예외사건 
try:
    n = int(input('Enter a number : '))
    print('OK. Your number is : ', n)
except ValueError:
    print('This is not a number.')

# 예제2 -> 올바른 값 입력 완료까지 지속
while True:
    try:
        n = int(input("Enter yout number: "))
        break
    except ValueError:
        print("This is not a number")
    
print('OK. Your number is : ', n)



