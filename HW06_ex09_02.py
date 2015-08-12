#!/usr/bin/env python
# HW06_ex09_02.py

# (1)
# Write a function called has_no_e that returns True if the given word doesn't
# have the letter "e" in it.
#   - write has_no_e
# (2)
# Modify your program from 9.1 to print only the words that have no "e" and
# compute the percentage of the words in the list have no "e."
#   - print each approved word on new line, followed at the end by the %
##############################################################################
# Imports

# Body
#def has_no_e(word):
#	if word.find('e') != -1:
#		return True
#	else:
#		return False
		
def has_no_e():
	total = 0
	num_e = 0
	fin = open('words.txt')
	for line in fin:
		s = line.split()
		total += 1
		for i in range (len(s)):
			if s[i].find('e') == -1:
				num_e +=1
				print (s[i]+"\r\n")
	
	total = total * 1.0
	print total
	print num_e
	percent = num_e/total * 100
	print 'percentage of words with no "e": ', 
	print  percent
	
##############################################################################
def main():
	# Call your function(s) here.
	has_no_e()

if __name__ == '__main__':
    main()
