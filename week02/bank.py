# Bank.py
# prompts the user to read in two money amounts and add them
# Author: Sandra Donatus

amount1 = int(input('Enter amount1 (in cent):'))
amount2 = int(input ('Enter amount2 (in cent):'))
answer = float(amount1 + amount2)
answer/100
print(f"The sum of these is: €{answer/100:0.2f}") #formats the answer to two decimal places