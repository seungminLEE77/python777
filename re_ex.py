import re

print('=== 정규 표현식 ===')

#일반 검색
text = '내 혈압은 12mmHg 입니다.'
print('120' in text)

#정규 표현식
pettern = r'\d+'

result = re.findall(pettern, text)

print(result)


print('=== 정규 표현식 : 기본 패턴 ===')
sample = 'abc123xyz456'

#숫자 찾기
print(re.findall(r'\d+', sample))
print(re. findall(r'[a-z]+',sample))

# + 1개 이상
# * 0개 이상
# ? 0개 또는 1개


print('=== 정규 표현식 : 특정 형식 찾기 ===')


data = '이메일은 test123@gmail.com 입니다.'

#이메일 형식 간단히 찾기
email_pettern = r'\w+@\w+\.\w+'
emails = re.findall(email_pettern, data)
print(emails)

# \w 문자 또는 숫자
# \@ @문자
# \. .은 정규식에서 특수 문자이기 때문에 \를 붙여야 함

print('=== 정규 표현식 : re모듈 주요 함수 ===')
#re.findall()
#re.search()

text = 'python 123 java 456'
result = re.search(r'\d+',text)
print(result.group())

print('=== 정규 표현식 : 문자열 치환(replace eotls re.sub) ===')

text2 = '가격은 12000원 입니다.'

#숫자 제거
new_text = re.sub(r'\d+','', text2)
print(new_text)


print('=== 정규식 vs 일반 문자열 처리 비교 ===')

text3 = '몸무게: 70kg, 키: 178cm'

#단순 split 사용
print(text3.split(","))

# 정규식으로 숫자만 추출
numbers = re.findall(r"\d+", text3)
print(numbers)


"""
정리:

- split은 구분자가 명확할 때 유리합니다.
- 정규식은 '형식이 일정한 패턴'을 찾을 때 유리합니다.
"""


print("\n===== 7단계: 정규식은 어디에 쓰일까? =====")

"""
데이터 분석에서 정규식은 다음과 같은 경우에 사용됩니다.

1. 크롤링 데이터에서 숫자만 추출
   예: "120mmHg" → 120

2. 단위 제거
   예: "170cm" → 170

3. 특정 형식 데이터 찾기
   예: 날짜 형식, 이메일 형식

4. 불필요한 특수문자 제거
"""

print("===== 최종 정리 =====")

"""
1. 정규식은 문자열 패턴을 찾기 위한 도구입니다.
2. re 모듈을 사용해야 합니다.
3. \d, \w, [], + 같은 기호를 조합해 패턴을 만듭니다.
4. 데이터 정제 단계에서 매우 자주 사용됩니다.
"""
