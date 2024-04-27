# Weekday.py
# A program that outputs whether or not today is a weekday
# Author: Sandra Donatus

import datetime

today = datetime.date.today()

if today.weekday() == 5 or today.weekday == 6: # 5 and 6 is Saturday and Sunday
    print("It is the weekend, yay!")
else:
    print("Yes, unfortunately today is a weekday")