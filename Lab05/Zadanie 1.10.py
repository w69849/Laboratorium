import datetime

year = int(input("Podaj rok: "))
month = int(input("Podaj miesiąc: "))
day = int(input("Podaj dzień: "))

date = datetime.date(year, month, day)

print("Dzień roku:", date.timetuple().tm_yday)
print("Numer tygodnia:", date.isocalendar()[1])
print("2 tygodnie przed:", date - datetime.timedelta(weeks=2))
print("2 tygodnie po:", date + datetime.timedelta(weeks=2))

days_until_sunday = (6 - date.weekday()) % 7
nearest_saturday = date + datetime.timedelta(days=days_until_sunday)

print("Najbliższa niedziela:", nearest_saturday)

date_with_hour = datetime.datetime(year, month, day, datetime.datetime.now().hour)

print("Czas unixowy bieżącej godziny w podanym dniu:", int(date_with_hour.timestamp()))
