'''
Description:
Welcome.

In this kata you are required to, given a string, 
replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.

Example
alphabet_position("The sunset sets at twelve o' clock.")
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" (as a string)
'''

def alphabet_position(text):
    alphabet_list = list('abcdefghijklmnopqrstuvwxyz')
    matched = ''
    for letters in text:
        if letters.isalpha():       #if letters is string 
            matched += str(alphabet_list.index(letters.lower()) + 1) + ' '
            
    return matched[0:len(matched)-1]    
      

# print(alphabet_position('The sun sets at twelve'))
alphabet_position('The sun sets at twelve')
