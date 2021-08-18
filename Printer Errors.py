'''my solution at top, very standard'''
# def printer_error(s):
# 	good_letters = [x for x in 'abcdefghijklm']
# 	count = len(s)
# 	errors = 0
# 	for letters in s:
# 		if letters not in good_letters:
# 			errors += 1
# 	return f'{errors}/{count}'
#
# printer_error('aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz')


'''hard to read solution'''
# def printer_errors(s):
# 	'''
# 	create a list and append it with each results of
# 	(for x in s) if (x doesn't exist in iterations of string 'abcdefghijklm')
#
# 	splits 'input string' to individual character strs and iterates over each
# 	compares to the str chrs of 'abcdefghijklm'. if input str char doesn't exist
# 	in 'abcd..' append temporary list.
#
# 	Get count of both 'error' characters and total length of str chrs in input string.
# 	use string formatting to display values errors/total
# 	'''
# 	return "{}/{}".format(len([x for x in s if x not in 'abcdefghijklm']), len(s))  #hella readable this one


'''second solution'''
def printer_error(s):
    errors = 0
    count = len(s)
    for i in s:
        '''compares string char in i to 'm' which will compare the ascii code
            so essentially any ascii code above 'm' will count as error and subsequently
            increase count of errors by 1'''
        if i > "m": #cleverrr
            errors += 1
    return str(errors) + "/" + str(count)
