import sys
import csv
import tkFileDialog

print '\n'
print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
print 'welcome to the email grabber!'
print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
print ''
print 'i\'m going to ask you for the csv file to enter. got it?'
try:
    raw_input('(press enter to continue)')
except SyntaxError:
    pass

f = tkFileDialog.askopenfilename()

print 'looks like you chose this file: ' + f + '\n'
file_input = open(f, "r")


print 'i\'ll be printing to \"output.txt\"\n'
file_output = open('output.txt', 'w')

counter = 0

for line in file_input:
	if counter > 2:
		currentline = line.split(',')
		file_output.write( currentline[1] + '@ufl.edu, ')
	counter += 1

file_input.close()
file_output.close()