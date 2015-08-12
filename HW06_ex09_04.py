#!/usr/bin/env python
# HW06_ex09_04.py

# (1)
# Write a function named uses_only that takes a word and a string of letters,
# and that returns True if the word contains only letters in the list.
#   - write uses_only
# (2)
# Can you make a sentence using only the letters acefhlo? Other than "Hoe
# alfalfa?"
#   - write function to assist you
#   - type favorite sentence(s) here:
#       1: Hello half leech face
#       2: cool cafe coffee
#       3: coach fell off hellhole
##############################################################################
# Imports

# Body
def uses_only(word, s):
	flag = True
	for letter in word:
		if letter not in s:
			return False
	return True
	
#		if word.find(s[i]) == -1:
#			flag = False
#		else:
#			flag = True
#			return True
#	return False
	
def word_maker():
	fin = open('words.txt')
	words_file_list = []
	for line in fin:
		words_file_list.append(line.strip('\r\n'))
	return words_file_list
	
def sentence_maker(words_file_list):
	count = 0
	for letter in words_file_list:
		if uses_only(letter, 'acefhlo'):
			count +=1
			print letter
	print count
##############################################################################
def main():
	words_file_list = word_maker()
	sentence_maker(words_file_list)
	
	
#	print uses_only("Hello", "abcd")
	
if __name__ == '__main__':
    main()
