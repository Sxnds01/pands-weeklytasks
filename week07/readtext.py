# Readtext.py
# Program to get letter count in a text file
# Author: Sandra Donatus

#f = open("exampletext.txt", "xt")
#f.close()

#f = open("exampletext.txt", "a")
#f.write("Text file example for the week seven weekly task")
#f.close()

def letterFrequency(fileName, letter):
	# open file in read mode
	file = open(fileName, 'r')

	# store content of the file in a variable
	text = file.read()

	# using count()
	return text.count(letter)


# call the function and display the letter count
print(letterFrequency('exampletext.txt', 'e'))

