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


print 'i\'ll be printing to \"output.txt\"'
file_output = open('output.txt', 'w')

counter = 0

sys.stdout.write('loading')

for line in file_input:
	if counter > 2:
		currentline = line.split(',')
		file_output.write( currentline[1] + '@ufl.edu, ')
		sys.stdout.write('.')
	counter += 1

print ' done!\n'
file_input.close()
file_output.close()