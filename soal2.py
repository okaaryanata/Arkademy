from datetime import date, timedelta, datetime
def betweenDays(date1,date2):
    d1 = datetime.strptime(date1,'%Y-%m-%d').date()
    d2 = datetime.strptime(date2,'%Y-%m-%d').date()
    d = d2 - d1
    for x in range(d.days + 1):
        print(d1 + timedelta(days=x))

betweenDays('2019-12-29','2020-01-02')