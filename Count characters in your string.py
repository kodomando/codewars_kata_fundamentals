'''The main idea is to count all the occurring characters
in a string. If you have a string like aba,
then the result should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result
should be empty object literal, {}.'''

def count(string):
    if not string:
        return {}
    if string:
        string_list = [chars for chars in string]
        unique_strings = set(string_list)
        return {unique_char:(string_list.count(unique_char)) for unique_char in string_list}


string = 'abaa'
count(string)