# accounts.py
# Program involves entering a 10 digit code and the program returning the code
# with the last four digits and the first six replaced with x's
# Author: Sandra Donatus

account_number = input('Enter 10 digit account number:')
mystring = 'xxxxxxxxxx'
new_str = account_number[6:] # index 6 to the end
first_piece = mystring[0:6] # index 1 to 6 (not including 6 though)
final_string = first_piece + new_str
print(final_string)


account_number = input('Enter account number:')
mystring = 'x'
new_str = account_number[-4:]
first_string = mystring[0:len(mystring)]
final_string = first_string + new_str
print(final_string)


