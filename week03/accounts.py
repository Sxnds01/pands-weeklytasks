# accounts.py
# Program involves entering a 10 digit code and the program returning the code
# with the last four digits and the first six replaced with x's
# Author: Sandra Donatus

account_number = input('Enter 10 digit account number:')
code = 'xxxxxxxxxx' # 10 x's for each number of the account
new_code = account_number[6:] # index 6 to the end
first_piece = code[0:6] # index 1 to 6 (not including 6 though)
final_code = first_piece + new_code
print(final_code)


account_number = input('Enter account number:')
code = 'x'
new_code = account_number[-4:] # last 4 numbers of account number
first_string = code[0:len(code)] # from 0 to however long the code is
final_code = first_string + new_code
print(final_code)


