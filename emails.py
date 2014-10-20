import sys
import csv
import tkFileDialog

# ans = input("drag and drop the csv file into the terminal. press enter to continue")
f = tkFileDialog.askopenfilename()

print "looks like you chose this file: " + f
file_input = open(f, "r")


print "i'll be printing to \"output.txt\""
file_output = open("output.txt", "w")

counter = 0

for line in file_input:
	if counter > 2:
		currentline = line.split(",")
		file_output.write( currentline[1] + '@ufl.edu, ')
	counter += + 1

file_input.close()
file_output.close()