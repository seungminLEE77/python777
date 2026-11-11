# python 유니코드 / 인코딩 핵심 정리

text = '파이썬'

print(text)#문자열 출력
print(len(text))#문자열 길이

#뮨자 <-> 변환 
print(ord('가'))# 문자를 유니코드 숫자로 변환
print(chr(44032))# 숫자를 다시 문자로 변환


#인코딩
#Encode : 문자열을 바이트(byte)로 바꾸는 작업
# 파일 저장이나 네트워크 전송 시 사용됨
encoded = text.encode('utf-8')
print(encoded)
print(type(encoded))

# decode : 인코딩의 반대과정 / 문자열로 다시 복원하는 과정
decoded = encoded.decode('utf-8')
print(decoded)
print(type(decoded))

# 인코딩이 맞지 않으면 오류 발생
try:
    wrong = encoded.decode('cp949')
    print(wrong)
except UnicodeDecodeError:
    print('인코딩 방식이 맞지 않아 오류 발생')

    # 클로저(Closure) 데코레이터(Decorator)

# 클로저 : 내부 함수가 자신이 정의된 외부 함수의 변수들을 기억하고, 외부 함수의 실행이 끝난 후에도 해당 변수를 사용할 수 있는 구조

print('==== 1단계: 함수 안에 함수 만들기 ====')
def outer():
    print("outer 함수가 실행되었습니다.")

    def inner():
        print('inner 함수가 실행되었습니다.')

    return inner # 함수 자체를 반환
#   return inner() # 함수를 실행하고 그 결과를 반환

func = outer() 
func()

print('\n==== 2단계: 클로저 ====')
# 클로저는 '외부 함수의 변수를 기억하는 내부 함수'
def make_multiplier(x):
    # x는 make_multiplier 함수의 지역 변수

    def multiplier(n):
        # 내부 함수 multiplier는
        # 바깥 함수의 변수 x를 사용할 수 있다.
        return x * n

    return multiplier
    
times3 = make_multiplier(3)
print(times3(10))
print(times3(5))

print('\n==== 3단계: 데코레이터 기본 구조 ====')

# 데코레이터는 '함수를 꾸며주는 함수'
# 내부 구조는 클로저와 매우 유사

def decorator(func):
    # func는 꾸며줄 함수

    def wrapper():
        print('함수 실행 전')
        func()
        print('함수 실행 후')

    return wrapper

@decorator
def say_hello():
    print('안녕하세요')

say_hello()

print('\n==== 4단계: 매개변수가 있는 데코레이터 ====')

def decorator_width_args(func):
    def wrapper(name):
        print('실행 전')
        func(name)
        print('실행 후')
        
    return wrapper

@decorator_width_args
def say_name(name):
    print('이름 :', name)

say_name('홍길동')

