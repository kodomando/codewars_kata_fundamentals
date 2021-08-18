def alphabet_position(text):
	alphabet_list = list('abcdefghijklmnopqrstuvwxyz')
	matched = ''
	for letters in text:
		if letters.isalpha():  # if letters is string
			matched += str(alphabet_list.index(letters.lower()) + 1) + ' '
	# print(matched)
	print(len(matched))
	print(matched[-1])
	return matched[0:len(matched) - 1]


print(alphabet_position('The sun sets at twelve'))