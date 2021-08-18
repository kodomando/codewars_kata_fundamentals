'''
Given: an array containing hashes of names

Return: a string formatted as a list of names 
separated by commas except for the last two names, 
which should be separated by an ampersand.

>>>Example:

namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'

namelist([ {'name': 'Bart'} ])
# returns 'Bart'

namelist([])
# returns ''
Note: all the hashes are pre-validated and will only contain A-Z, a-z, '-' and '.'.
'''

#Code
names = [{'name': 'Bart'},
         {'name': 'Lisa'},
         {'name': 'Maggie'},
         {'name': 'Homer'},
         {'name': 'Dillion'},
         {'name': 'Sarge'},
         {'name': 'Martell'},
         {'name': 'Cory'},
         {'name': 'Svanson'},
         {'name': 'Miguel'}
         ]


def namelist(names):
	name_list = [values for dicts in names for values in dicts.values()]
	length = len(name_list)

	if length == False:
		return ''

	if length == 1:
		return f'{name_list[0]}'

	if length == 2:
		return f'{name_list[0]} & {name_list[1]}'

	if length > 2:
		_ = ', '.join(name_list[:-1])
		return f'{_} & {name_list[-1]}'


# return [name for index, name in enumerate(name_list[:-1])]
# print(f"{name}, and {name_list[-1]}, end=' '")

print(namelist(names))
