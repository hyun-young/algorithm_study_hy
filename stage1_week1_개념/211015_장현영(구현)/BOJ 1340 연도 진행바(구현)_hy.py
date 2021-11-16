# MONTH DD, YYYY, HH:MM
# 연도는 1800보다 크거나 같고, 2600보다 작거나 같다. (input엔 올바른 형식이 들어감)
# 현재 달 입력하면 퍼센트 출력하는 것
# 평년은 365일 윤년 366일임을 확인하고나서 퍼센트를 출력!
import sys

month, day, year, time = sys.stdin.readline().split()

# 'May', '10,', '1981', '00:31' 형태로 저장된 것을 모두 정수형으로 수정
month_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# month
months_dict = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8, 'September': 9,\
    'October': 10, 'November': 11, 'December': 12}

mon = months_dict[month] # key가 index 역할

# day
day = int(day[:-1]) # str 형태이므로 슬라이싱하기 --> 마지막 ,빼기 ---int 형태로 변환
year = int(year)
# 00~ 09 형태도 int로 변환 가능!
hour = int(time[0:2])
minute = int(time[3:])

# 윤년 계산
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    month_day[1] = 29 # 2월만 day 변경

# 날짜 계산 ex> 5월 10일 이면 5월 9일까지 날짜 수(4월30일까지, + 9일)
total = sum(month_day[:mon-1]) + (day-1)
total += (minute*(1/(60*24)) + hour*(1/24))
print(total / sum(month_day) * 100)