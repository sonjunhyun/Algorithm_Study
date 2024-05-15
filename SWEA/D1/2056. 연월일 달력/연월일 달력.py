days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range(1, int(input())+1):
    dates = [str(date) for date in input().split()]
    for date in dates:
        year = date[:4]
        month = date[4:6]
        day = date[6:]
        
        if int(month) not in range(1, 13):
            result = -1
        elif int(day) == 0 or int(day) > days[int(month)-1]:
            result = -1
        else:
            result = f"{year}/{month}/{day}"
            
    print(f"#{i} {result}")