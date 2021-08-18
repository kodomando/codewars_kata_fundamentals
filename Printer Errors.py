'''In a factory a printer prints labels for boxes. 
For one kind of boxes the printer has to use colors which, 
for the sake of simplicity, are named with letters from a to m.

The colors used by the printer are recorded in a control string.
For example a "good" control string would be aaabbbbhaijjjm
meaning that the printer used three times color a, four times color b, one time color h then one time color a...

Sometimes there are problems: lack of colors, 
technical malfunction and a "bad" control string is produced 
e.g. aaaxbbbbyyhwawiwjjjwwm with letters not from a to m.

You have to write a function printer_error which given 
a string will return the error rate of the printer as 
a string representing a rational whose numerator is 
the number of errors and the denominator the length 
of the control string. Don't reduce this fraction 
to a simpler expression.

The string has a length greater or equal to one and 
contains only letters from ato z.

Examples:
s="aaabbbbhaijjjm"
printer_error(s) => "0/14"

s="aaaxbbbbyyhwawiwjjjwwm"
printer_error(s) => "8/22"
'''


'''my solution at top, very standard'''
def printer_error(s):
 	good_letters = [x for x in 'abcdefghijklm']
 	count = len(s)
 	errors = 0
 	for letters in s:
 		if letters not in good_letters:
 			errors += 1
return f'{errors}/{count}'

 printer_error('aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz')


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

   
'''kinda of hard to read solution, this one was really cool'''
def printer_errors(s):
   #create a list and append it with each results of
   (for x in s) if (x doesn't exist in iterations of string 'abcdefghijklm')

   '''splits 'input string' to individual character strs and iterates over each
   #compares to the str chrs of 'abcdefghijklm'. if input str char doesn't exist
   in 'abcd..' append temporary list.

Get count of both 'error' characters and total length of str chrs in input string.
   use string formatting to display values errors/total'''

   return "{}/{}".format(len([x for x in s if x not in 'abcdefghijklm']), len(s))
   #damn son... dat use of list comprehension ::flame emoji::
   #it's quite readable too, taking notes!
