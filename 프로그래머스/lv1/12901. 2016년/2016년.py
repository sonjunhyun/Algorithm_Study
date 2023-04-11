def solution(a, b):
    day_of_week = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    days_of_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    date_diff = sum(days_of_month[:a - 1]) + b - 1
    return day_of_week[date_diff % 7]