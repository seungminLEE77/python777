#print("hi")
# 문제 : `안녕하세요.`를 10번 출력해주세요.
# "",'' 안에 있는 문자는 문자로 출력된다.
# \n 줄바꿈 단축키
#print("안녕하세요.\n" *10)
#print(10+10)
# 문제 : `안녕하세요.`를 10번 출력해주세요.
# 조건 : print 딱 한번만 사용 가능
# 조건 : \n 을 활용해서 줄바꿈 해주세요.
# 힌트 : \n 은 줄바꿈을 의미합니다.

#text = "안녕하세요.\n"
#print (text *10)

# 변수 = 미지수
# 변수에는 값 오직 하나
# = 기준으로 좌측에 있을 때만 변수

#x = 10
#print(x) # 10

#x = 6
#print(x) # 6

#x = 7
#print(x) # 7

'''
x=10
y=5

print(x)
print(y)

x=5
y=10

print(x) #5  
print(y) #10

print(f"x : {x}")
print(f"y : {y}")
'''

#x = 10
#y = 5 
'''
print(f"x : {x}")
print(f"y : {y}")

z = x # 변수 z 지정후 x값 저장
x = y 
y = z

print(f"x : {x}")
print(f"y : {y}")
'''
# 불리언 true / false, t/f - 조건문 사용
# 문자열 : "안녕" 리스트 : 여러개 넣을수있다 변경 가능 튜플: 여러개 변경 불가능

# int 숫자정수 , string 문자열 , float 실수
# 자료형 변환
'''
a = 10
b = 20
#문자열로 변경 str()
print(str(a) +str(b))
# 출력 => 1020


a = '3'
b = '6'
# 정수형으로 변경 int()
print(int(a) +int(b))
# 출력 9

a = '3.1'
b = '6.1'
#실수형으로 변경 float() 깨끗한 실수형만 변환 가능
print(float(a) +float(b))
# 출력 9.2


a = '3.1'
b = '6.1'

#a=float(a)
#b=float(b)
#a=int(a)
#b=int(b)
# 실수형으로 변경후  실수형으로 계산 (int(float())
print(int(float(a))+int(float(b)))
# 출력 9


print('안녕')
input()
print('잘가')


# 문제 - 사용자에게 문장 1개를 입력받아서, ','를 기준으로 나눠주세요.
print("문장을 입력해 주세요", end=':')
line=input()

l = line.split(',')
print(l)

# 문제 - 사용자에게 문장 1개를 입력받아서, strip 한 결과를, 다시 ','를 기준으로 나눠주세요.
print("문장을 입력해 주세요", end=':')
l = input() #.strip().split(',')
l = l.strip()
l= l.split(',')


print(l)
'''
'''
# 문제 : 사용자에게 숫자 3개를 입력받아서, 더한 결과를 출력해주세요. map, strip를 사용해주세요.

print("숫자 세개를 입력해주세요")
print("문장 사이에 , 를 입력해주세요", end = ':')
a, b, c = map(int, input().strip().split(','))


print(a+b+c)

a=int(l[0])
b=int(l[1])
c=int(l[2])


print(l)
'''

#조건문 
#and 기준이 엄격함 Ture or Ture = Ture
#or 조금 느슨함 둘중 하다만 참이면 참

# age = 10
'''
if age >= 20:
    print('성인입니다')

if age < 20:
    print('미성년입니다')

if 조건식:
    실행문


age = 10 
if age == 10:
    print('10입니다')
if age == 20:
    print('20입니다')
if age == 30:
    print('30입니다')
    '''
'''
 #문제시작
a = 10

# `==` => 같다.
if ( a == 10 ):
  print("참")

# `!=` => 같지 않다.
if ( a != 10 ):
  print("거짓")

if ( a > 10 ):
  print("거짓")

if ( a >= 10 ):
  print("참")

b = 10

if ( a == b ):
  print("참")

# c 에는 true or false 이 담긴다.
c = a != b

if ( c ):
  print("거짓")

if ( c == False ):
  print("참")

# `not` => 반전
if ( not c ):
  print("참")

if ( not(not c) ):
  print("거짓")

d = True

if ( c != d ):
  print("참")

if ( 10 > 5 and -6 > -10 and 10 != 10 ):
  print("거짓")

if ( 10 < 5 and -6 < -10 and 10 != 10 or 10 > 5 ):
  print("참")
  '''

  
# 문제 : 할인 대상인지 아닌지 출력해주세요.
# 조건 : 나이가 19세 이하이거나 60세 이상이면 할인 대상입니다.
# 조건 : `and, or`없이 풀어야 합니다.
# 조건 : 2가지 이상의 방법으로 풀어야 합니다.
'''
age = 33

print("== 정답 v1 ==")

if age <= 19:
  print("할인 대상입니다.")

if age >= 60:
  print("할인 대상입니다.")

if age > 19:
  if age < 60:
    print("할인 대상이 아닙니다.")

print("== 정답 v2 ==")

if age < 20:
  print("할인 대상입니다.")
elif age >= 60:
  print("할인 대상입니다.")
else:
  print("할인 대상이 아닙니다.")

# 반복문
#while문 조건 3가지 1. 시작값 2. 끝 값/조건식 3. 보폭*** i = i + 1 보폭이 없을경우 무한루프에 빠진다.
i = 1
while i <= 3:
  print(i)
  i = i + 1

print(i)

# 문제 : 1부터 300까지 출력해주세요.

i = 1
while i <= 300:
  print(i)
  i = i + 1

# 문제 : 100부터 -25까지 출력해주세요.

i = 100
while i >= -25:
  print(i)
  i = i - 1
'''
  # 문제 : 1부터 100 사이의 짝수만 출력해주세요.(개념 : while, if, %)

i = 2 # % 사용하면 i = 1 
while i <= 100:
    #if i % 2 == 0: 짝수 출력 공식
    print(i)
    i += 2



# 문제 : 1부터 1000 사이의 수 중에서 3의 배수만 출력해주세요.

i = 3 # % 사용하면 i = 1
while i <= 1000:
    #if i % 3 == 0: 3의 배수 출력 공식
    print(i)
    i += 3

# 문제 : 1부터 5까지의 합을 출력해주세요.(개념 : while)

k = 0
i = 1
while i <= 5:
    k += i
    i += 1
print(k)

# 문제 : 1부터 100까지의 수 중에서 짝수의 합을 출력해주세요.(개념 : while, if, %)

p = 0
i = 2 # % 사용하면 i = 1 
while i <= 100:
    #if i % 2 == 0:
    p += i
    i += 2
print(p) # 중간에 값을 확인하고싶으면 while 아래쪽에 print 삽입, 결과만 알고싶다면 

# 문제 : 1부터 3까지 10번 반복해서 출력해주세요.
i = 1
while i <= 10:
    j = 1
    while j <= 3:
        print(j)
        j += 1
    print("=====")
    i += 1

    #while : 조건식이 참인 동안 반복 (조건에 따른 반복)
    #for : 정해진 범위나 데이터의 요소를 순서대로 반복
    # range(stop) : 0 부터 종료값 직전까지
    # range(start, stop) : 시작값부터 종료값 직전까지
    # range (start, stop, step) : 시작값부터 종료값 직전까지 정해진 보폭 만큼
for i in  range(1, 5, 2):
    print(i)

i = 1 
while i < 5:
    print(i)
    i += 2

# 문제 : for문으로 1부터 100까지 출력

for i in range(1, 101):
    print(i)
   
# 문제 : for문으로 100부터 1까지 출력


for i in range(100, 0, -1):
    print(i)

# 문제 : for문으로 구구단 1단 ~ 9단 출력
#for dan in range(1, 10):
    #print(f'= {dan}단' ==)
    #for i in range(1, 10):
        #print(f'{dan} * {i} = {dan*i}')

    
def a():
    for i in range(1, 6):
        print(i)

a()
a()



# 문제 : 함수를 사용해서 코드량을 확 줄여주세요.

dan = 8

def print_n_dan(dan): # 매개변수 parameter
    
     i = 1
     while i <= 9:
         print("{} * {} = {}".format(dan, i, dan * i))
         i += 1

     print("== 1번째 구구단 8단 출력 ==")
     

print_n_dan(3) #인자 인수 argument


# 문제 : 함수를 사용해서 코드량을 확 줄여주세요.
def print_n_dan(dan):
   
     print("== {}단 ==".format(dan))
     i = 1
     while i <= 9:
      print("{} * {} = {}".format(dan, i, dan * i))
      i += 1


print_n_dan(1)
print_n_dan(2)
print_n_dan(3)
print_n_dan(4)
print_n_dan(5)
print_n_dan(6)
print_n_dan(7)
print_n_dan(8)
print_n_dan(9)
print_n_dan(10)



# 함수가 값을 가지게 하려면 딱 하나 [리턴:반환값]
# 리턴 : 함수에서 처리한 결과를 함수 외부로 전달하고,함수를 종료시키는 키워드 
def add(a, b):
    print(a+b)
    return 'end'
x = add(10,20)
print(f'x : {x}')



