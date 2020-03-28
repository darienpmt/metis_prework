import calendar

def weekDay(dt):
    dt = dt.split()
    day = calendar.weekday(int(dt[2]), int(dt[0]), int(dt[1]))
    print(calendar.day_name[day].upper())


print(weekDay('08 05 2015'))