from openpyxl import *

# == 시트 생성 ==

w2 = load_workbook('test.xlsx')

#새로운 시트 하나 생성
new_ws.title = '마지막 시트'

rom openpyxl import *

# == 시트 생성 ==

w2 = load_workbook('openpyxl/test.xlsx')

# 새로운 시트 하나 생성

new_ws = w2.create_sheet()

# 새로 만든 시트의 이름 설정

# 기본 이름 : Sheet1, Sheet2

new_ws.title = '마지막_시트'

# 변경사항 저장

w2.save('test.xlsx')

from openpyxl import *
from openpyxl.styles import PatternFill

# == 셀 배경 색 바꾸기 == 

wb = Workbook()
ws = wb.active
# 헤더


ws['A1'] = '이름'
ws['B1'] = '국어'
ws['C1'] = '수학'


color = PatternFill(fill_type='solid', fgColor='FFFF00')

# 반복문을 통해 셀의 배경색 바꾸기
for cell in ws[1]: # 1행 전체
    cell.fill = color
wb.save('openpyxl/bg_color.xlsx')

# 색상 코드
# 빨강 : FF0000
# 노랑 : FFFF00
# 초록 : 00FF00
# 파랑 : 0000FF
# 회색 : D9D9D9