# Collatz.py
# Program where user inputs any positive integer and then outputs successive values
# If the value is even, divide the successive value by two
# If the value is odd, multiply it by three and add one
# End the program on the value of one
# Author: Sandra Donatus
'''
input_num = int(input("Enter a number:\n")) #\n to put on a separate line
def collatz (num):
    collatz = (input_num)
    while (num !=1):
        if(num %2 == 0):
            num = num/2
        print(num)
    else:
        num = 3*num+1
        print(num)
'''    

def collatz(num): #defines the function
    sequence =[num]
    while (num!=1):
        if(num %2 == 0):
            num = num/2
            sequence.append(num) #adds the outputs into the square brackets: [num]
        else:
            num = 3*num+1
            sequence.append(num)

    return sequence
print(collatz(30))