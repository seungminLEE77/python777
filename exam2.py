# 문제 : 입력받은 정수가 소수인지 아닌지 알려주는 함수를 구현해주세요.

def get_divisors_sum(num):
  s = 0
  i = 1
  while i <= num:
    if num % i == 0:
      s += i
    i += 1
  return s

def is_prime_number(num):
  if num == 1:
    return False

  i = 2
  while i < num:
    if num % i == 0:
      return False
    i += 1
    
  return True

def is_prime_number_v2(num):
  return get_divisors_sum(num) == num + 1 # 약수의 합

print("3은 소수입니다 : {}".format(is_prime_number(3)))
print("4는 소수입니다 : {}".format(is_prime_number(4)))
print("1000은 소수입니다 : {}".format(is_prime_number(1000)))


# 문제 : 리스트에 순서대로 2, 1, 5, 6, 7를 한 번에 담아주세요.
a = [2, 1, 5, 6, 7]

print(a)

# 문제 : 비어있는 리스트를 만들고, 순서대로 2, 1, 5, 6, 7를 하나씩 담아주세요.
a = []

a.append(2)
a.append(1)
a.append(5)
a.append(6)
a.append(7)

print(a)

# 문제 : 리스트에 순서대로 '월', '화', '수', '목', '금'을 한번에 담아주세요. 그리고 '+=' 연산자를 이용해서 '토', '일' 을 한번에 추가해주세요.

a = ['월', '화', '수', '목', '금']
a += ['토', '일']
print(a)

# 문제 : 리스트에 순서대로 '월', '화', '수', '목', '금'을 한번에 담아주세요. 그리고 가장 마지막 요소를 출력해주세요.

a = ['월', '화', '수', '목', '금']

#print(a[4])
print(a[-1])
l = len(a)
print(a[l-1])

# 문제 : 리스트에 순서대로 '월', '화', '수', '목', '금'을 한번에 담아주세요. 그리고 while문을 이용해서 요소 전부 출력해주세요.

a = ['월', '화', '수', '목', '금']

i = 0
while i < len(a):
  print(a[i])
  i += 1

# 문제 : 리스트에 순서대로 2, 1, '오', 6, 7를 한번에 담아주세요. 그리고 리스트 안에 있는 '오'를 정수 5로 변경해주세요.


a = [2, 1, '오', 6, 7]

#a[2] = 5
a[a.index('오')] = 5

print(a)

# 문제 : 리스트에 순서대로 '월', '화', '수', '목', '금'을 한번에 담아주세요. '화'가 리스트 안에 들어있는지 알려주세요.


a = ['월', '화', '수', '목', '금']

if '화' in a:
  print('있다')
else:
  print('없다')





# 문제 : 리스트에 순서대로 '월', '화', '수', '목', '금'을 한번에 담아주세요. '화'가 리스트 안에서 몇 번째 데이터 인지 알려주세요.

a = ['월', '화', '수', '목', '금']



print(a.index('화'))




a = ['월', '화', '수', '목', '금']

#del a[4]
#del a[-1]
#del a[a.index('금')]
a.remove('금')

print(a)


# 문제 : 딕셔너리에 각 달의 마지막 날들을 한번에 담기

mon = {"1월": 31, "2월": 28, "3월": 31}

print(mon)

# 문제 : 딕셔너리에 각 달의 마지막 날들을 반복문을 통해 담기
mon = {}

mon["1월"] = 31
mon["2월"] = 28
mon["3월"] = 31

print(mon)

print("== 정답 v2 ==")
month_end_days = {}

for i in range(1, 12 + 1):
  month = str(i) + "월"

  end_day = 31

  if i == 2:
    end_day = 28
  elif i in [4, 6, 9, 11]:
    end_day = 30

  month_end_days[month] = end_day

print(month_end_days)

print("== 정답 v3 ==")
month_end_days = {}

month_end_days_list_ver = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i, end_day in enumerate(month_end_days_list_ver):
  month = str(i + 1) + "월"
  month_end_days[month] = end_day

print(month_end_days)

# 인덱싱 : 특정 위치의 문자 하나를 가져오는 것
# 슬라이싱 : 지정한 범위의 문자열을 가져오는 것

print("== 예제 1 ==")
s = "안녕하세요."
#   [0,1,2,3,4,5]

print("s길이 출력")
print(len(s))

# s[start:end(-1):step]
print("s를 이루는 문장 중에서 앞에 거 2개 출력")
print(s[0:2])

print("s를 이루는 문장 중에서 문자 하나 건너 뛰고 1개 출력")
print(s[1:2])

print("s를 이루는 문장 중에서 문자 4개 출력, 첫 인덱스 생략")
print(s[:4])

print("s를 이루는 문장 중에서 앞에 문자 3개 건너 뛰고, 나머지 전부 출력, len")
print(s[3:len(s)])

print("s를 이루는 문장 중에서 앞에 문자 3개 건너 뛰고, 뒤 인덱스 생략")
print(s[3:])


print("== 예제 2 ==")
s = "안녕하세요."

print("s를 이루는 문자를 하나씩 출력, while")
i = 0
while i < len(s):
    print(s[i])
    i += 1

print("s를 이루는 문자를 역순으로 하나씩 출력, while")
i = len(s) - 1
while i >= 0:
    print(s[i])
    i -= 1

print("s를 이루는 문자를 하나씩 출력, for")
for c in s:
    print(c)



s = '안녕하세요'
i = 0
while i < len(s):
  print(s[i])
  i += 1

s = '안녕하세요'

i = len(s)-1 # 역순으로 출력
while i >= 0:
  print(s[i])
  i -= 1

s = '안녕하세요'
for c in s:
  print(c)


print('예제 3번')
print('s를 이루는 문장 중에서 한글만 출력')

s = 'a안b녕c하d세e요'
print(s[1]+ s[3]+ s[5]+ s[7]+ s[9])

print('s를 이루는 문장 중에서 한글만 출력, for, if, or, continue')
for c in s:
  if c == 'a' or c == 'b' or c == 'c' or c == 'd' or c == 'e' or c == 'f':
   continue
print(c)

print('s를 이루는 문장 중에서 한글만 출력, for, if, and')
for c in s:
  if c != 'a' and c != 'b' and c != 'c' and c != 'd' and c != 'e' and c != 'f':
    print(c)


print("s를 이루는 문장 중에서 한글만 출력, for, not in, 방법 3")
for c in s:
    if c not in ['a', 'b', 'c', 'd', 'e', 'f']:
        print(c)


#클래스 

class Person:
  def Hello(self):
    print("Hi")

jin = Person() # jin은 Person의 인스턴스

jin.Hello()

print(type(jin))


a = int(10)
b = list(range(10))

b.append(20)

print(b)


a = 10
print(type(a))

b = [1, 2, 3]
print(type(b))

c = {"x" : 1, "y" : 2}
print(type(c))


a = list(range(10))
b = list(range(20))

# a, b는 객체다.
# a, b는 list의 클래스의 인스턴스다.

class Person:
  pass

class Person:
  def Hello(self):
    print("Hello")

  def hi(self):
    self.Hello()

jin = Person()
jin.hi()


class Person():
  def __init__(self, name, age, hobby): # 이 안에 있는 속성은 인스턴스 속성이다.
    self.hello = '안녕하세요'
    self.name = name
    self.age = age
    self.hobby = hobby

  def introduce(self):
    print("{}, 저는 {} 입니다.".format(self.hello,self.name)) # 클래스 내부에서 접근

jin = Person('진', 22, '운동')
jin.introduce()

paul = Person('폴', 33, '요리')

print("== 진 ==")
print('이름 : {}'.format(jin.name)) # 클래스 외부에서 접근
print('나이 : {}'.format(jin.age))
print('취미 : {}'.format(jin.hobby))

print("== 폴 ==")
print('이름 : {}'.format(paul.name))
print('나이 : {}'.format(paul.age))
print('취미 : {}'.format(paul.hobby))


class Person:
  pass
jin = Person()# 인스턴스 생성
jin.name = '진' # 인스턴스를 생성한 뒤 속성 추가



print(jin.name)

#클래스 외부에서는 접근 불가, 클래스 내부에서만 사용 가능한 private attribute

class Person():
  def __init__(self, name, age, hobby, weight): #인스턴스 속성
    self.hello = '안녕하세요'
    self.name = name
    self.age = age
    self.hobby = hobby
    self.__weight = weight # 변수 앞에 __ 를 붙이면 비공개 속성으로 변경

  def diet(self, loss_weight):
    self.__weight -= loss_weight
    print("{} kg 입니다.".format(self.__weight))

jin = Person('진', 22, '운동', 78)
jin.diet(20)


class Person():

  folder = [] #클래스 속성 

  def add_files(self, file):
      self.folder.append(file)

jin = Person()
jin.add_files('text')

kim = Person()
kim.add_files('img')

print(jin.folder)
print(kim.folder)



class Person:
  __weight = 78

  def print_weight(self):
    print(Person.__weight)

jin = Person()
jin.print_weight()

print(jin.__weight)

print('hi')


