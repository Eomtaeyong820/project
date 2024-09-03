#파이썬 3가지 Print Formmating

x = 50
y = 100
text = 308276567
n = 'Eom' 

#출력 1
ex1 = 'n = %s, s= %s sum=%d' % (n, text, (x+y))
print(ex1)

#출력 2
ex2 = 'n = {n}, s = {s}, sum = {sum}'.format(n=n, s=text, sum=x+y)
print(ex2)

#출력 3 -> f스트링 f작성 후 ''로 묶고 변수 설정하면 됨 가장 간단함 
ex3 = f'n={n}, s={text}, sum={x+y}'
print(ex3)

print(f'n={n}, s={text}, sum={x+y}') # 이런식으로 바로 출력 할 수도 있음

#구분기호
m = 100000000
print(f'm: {m:,}') #천 단위로 구분해서 출력됨 

#정렬
# ^:가운데 정렬, <:왼쪽 정렬, >:오른쪽 정렬

t=20
print(f't : {t:10}') 
print(f't : 가운데 {t:^10}')
print(f't : 왼쪽 {t:<10}')
print(f't : 오른쪽 {t:>10}')

print(f't : {t:*^10}') #10자릿수중 20의 두 자릿수를 제외하고 *로 채움
print(f't : {t:$<10}') #10자릿수중 20의 두 자릿수를 제외하고 $로 채움



