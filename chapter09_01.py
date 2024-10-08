# Chapter09-1
# 파일 읽기 및 쓰기

# 읽기모드: r , 쓰기모드: w, 추가모드: a, 텍스트 모드: t, 바이너리 모드: b
#  상대 경로('../, ./'), 절대 경로('C:\Django\example..')

# 파일 읽기(Read)
# 예제1

f = open('./resource/it_news.txt', 'r', encoding='UTF-8')
# 속성 확인
print(dir(f))
# 인코딩 확인 기본값은 utf-8이다
print(f.encoding)
# 파일 이름
print(f.name)
# 모드 확인
print(f.mode)
cts = f.read()
print(cts)
# 반드시 close
f.close()

# 예제2
with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    c = f.read()
    print(c)
    print(iter(c))
    print(list(c))
# with문을 사용하면 close를 사용하지않아도 내부적으로 리소스가 닫힘

# 예제3
# read(): 전체 읽기, read(10) : 10Byte -> 바이트 수에 맞는 문자를 읽음

with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    c = f.read(20)
    print(c)
    c = f.read(20)
    print(c)
    c = f.read(20)
    print(c)
    f.seek(0,0) # 처음 커서로 돌아감
    c = f.read(20)
    print(c)

# 예제4
with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    line = f.readline()
    print(line)
    line = f.readline()
    print(line)

# 예제5
# readlines : 전체를 읽은 후 라인 단위 리스트로 저장

with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    cts = f.readlines()
    print(cts)
    print()
    for c in cts:
        print(c, end='')

# 파일 쓰기(write)

# 예제1
with open('./resource/contests1.txt', 'w') as f:
    f.write('I love python\n')

# 예제2
with open('./resource/contest1.txt', 'a') as f:
    f.write('I love python2\n') # a사용시 기존의 내용에 덮어써지는게 아니라 추가됨

# 예제3
# writelines : 리스트 -> 파일
with open('./resource/contests2.txt', 'w') as f:
    list = ['Orange\n', 'Apple\n', 'Banana\n', 'Melon\n']
    f.writelines(list)

# 예제4  -> 자주 사용은 안하지만 기억만 해두기
with open('./resource/contents3.txt', 'w') as f:
    print('Test text Write', file=f)
    print('Test text Write', file=f)
    print('Test text Write', file=f)

