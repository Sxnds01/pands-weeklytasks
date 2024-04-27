# Squareroot.py
# Write a program that takes a positive floating-point number and outputs its square root
# Author: Sandra Donatus

#number = input('Please enter a positive number:') - always get errors when using this function
number = 100
def squareroot(number):
    print(number)
    return(number**(1/2)) #the square root of a number is equal to the power of a half - 1/2

ans = squareroot(100)
print(f'The square root of {number} is approx. {ans}')