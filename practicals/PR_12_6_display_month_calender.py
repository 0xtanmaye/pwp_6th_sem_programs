import calendar
year = int(input("Enter the year: "))
month = int(input("Enter the month (1-12): "))
cal = calendar.TextCalendar(calendar.SUNDAY)
print(cal.formatmonth(year, month))
