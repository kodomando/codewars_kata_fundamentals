from collections import *
import numpy as np

#got this duplicate_count code from stackoverflow
#not sure how efficient it is, should probably look into making
#own version later, hopefully much shorter
def duplicate_count(text, *number):
	def convert_to_words(num):
		l = len(num)

		if (l == 0):
			print('empty string')
			return

		if (l > 4):
			print('does not support above 9999')
			return

		single_digits = ["zero", "one", "two", "three",
		                 "four", "five", "six", "seven",
		                 "eight", "nine"]

		two_digits = ["", "ten", "eleven", "twelve",
		              "thirteen", "fourteen", "fifteen",
		              "sixteen", "seventeen", "eighteen",
		              "nineteen"]

		tens_multiple = ["", "", "twenty", "thirty", "forty",
		                 "fifty", "sixty", "seventy", "eighty",
		                 "ninety"]

		tens_power = ["hundred", "thousand"]

		# For single digit number
		if (l == 1):
			print(single_digits[ord(num[0]) - 48])
			return

		# Iterate while num is not '\0'
		x = 0
		while (x < len(num)):

			# Code path for first 2 digits
			if (l >= 3):
				if (ord(num[x]) - 48 != 0):
					print(single_digits[ord(num[x]) - 48],
					      end=" ")
					print(tens_power[l - 3], end=" ")
				# here len can be 3 or 4

				l -= 1

			# Code path for last 2 digits
			else:

				# Need to explicitly handle
				# 10-19. Sum of the two digits
				# is used as index of "two_digits"
				# array of strings
				if (ord(num[x]) - 48 == 1):
					sum = (ord(num[x]) - 48 +
					       ord(num[x + 1]) - 48)
					print(two_digits[sum])
					return

				# Need to explicitely handle 20
				elif (ord(num[x]) - 48 == 2 and
				      ord(num[x + 1]) - 48 == 0):
					print("twenty")
					return

				# Rest of the two digit
				# numbers i.e., 21 to 99
				else:
					i = ord(num[x]) - 48
					if (i > 0):
						print(tens_multiple[i], end=" ")
					else:
						print("", end="")
					x += 1
					if (ord(num[x]) - 48 != 0):
						print(single_digits[ord(num[x]) - 48])
			x += 1

	# remove spaces
	text.strip()
	# find unique elements in str
	text_unique = list(set(text))
	# get length of list with unique elements
	len_unq = len(text_unique)
	# tuple of unique str and it's total count in the string
	# duplicates_list =  (Counter(text).most_common(len_unq))
	duplicates_list = [(x, y) for x, y in Counter(text).most_common(len_unq) if y > 1]
	# duplicates_np = np.array(duplicates_list)
	# duplicates_dict = dict((x, y) for x, y in duplicates_list)
	# print(duplicates_list, '\n')
	

	# print(bool(duplicates_list))
	if not duplicates_list:
		print('no characters repeats more than once')

	if duplicates_list:
		# print('there is something')
		output = []
		for i, data in enumerate(duplicates_list):
			# print(i, data)
			# conv = convert_to_words(str(duplicates_list[i][1]))

			if len_unq == 1:
				a = "'{}' occurs '{}' times".format(duplicates_list[i][0], duplicates_list[i][1])
				output.append(a)
				# convert_to_words(str(duplicates_list[i][1]))
			if len_unq == 2:
				a = "'{}' occurs '{}' times".format(duplicates_list[i][0], duplicates_list[i][1])
				output.append(a)

			if len_unq > 2:
				a = "'{}' occurs '{}' times".format(duplicates_list[i][0], duplicates_list[i][1])
				output.append(a)

		#         [print(i) for i in b]

		if len_unq == 1:
			print(output[0])
		if len_unq == 2:
			print(' and '.join(output))
		if len_unq > 2:
			print(' and '.join(output))


#             if len_unq > 1:
#                 print('{} # {} occurs {} times'.format(len_unq, duplicates_np[i,:1], duplicates_np[i,1]))
# #         for key, value in duplicates_dict.items():
#             if len_unq == 1:
#                 print('{} # {} occurs {} times'.format(len_unq, key, value))
#             elif len_unq > 2:
#                 print('{} # {} and {} times'.format(len_unq, key, value))


#     print(text_unique)
#     print(duplicates)

#     if duplicates:
#         print(len(duplciates))
#     else:
#         pass

duplicate_count('')  # 0
duplicate_count('ccccccccccccccc')  # 1
duplicate_count('BBBcccc')  # 2
duplicate_count('BBBaaaabbb')    #2_1
duplicate_count('BBBBcccCc')   #2_2
duplicate_count('BBBBBBcccaaaaaaaaaeeeeee')
