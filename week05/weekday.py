import datetime

today = datetime.date.today()

if today.weekday() == 5 or today.weekday == 6:
    print("It is the weekend, yay!")
else:
    print("Yes, unfortunately today is a weekday")