'''The word i18n is a common abbreviation of internationalization
in the developer community, used instead of typing the whole
word and trying to spell it correctly. Similarly, a11y is an
abbreviation of accessibility.

Write a function that takes a string and turns any and all
"words" (see below) within that string of length 4 or greater
into an abbreviation, following these rules:

A "word" is a sequence of alphabetical characters. By this definition,
any other character like a space or hyphen (eg. "elephant-ride")
will split up a series of letters into two words (eg. "elephant" and "ride").
The abbreviated version of the word should have the first letter,
then the number of removed characters, then the last letter
(eg. "elephant ride" => "e6t r2e").
'''
import re
from timeit import default_timer as timer

start = timer()

def abbreviate(s):
    def abbr(string):
        return (string[0] + str(len(string[1:-1])) + string[-1])
    split = re.split(r'([^a-zA-Z])', s)
    return "".join([abbr(string) if string.isalpha() and len(string) >= 4 else string for string in split])

    '''Without List Comprehension'''
    # new = []
    # for string in split:
    #     if string.isalnum():
    #         new.append(string[0] + str(len(string[1:-2])) + string[1])
    #     else:
    #         new.append(string)

string = "sat. balloon, monolithic. balloon. monolithic is, doggy-cat5balloon5"
print(abbreviate(string))

end = timer()
time_elapsed = end - start
print(f"Time elapsed: {time_elapsed:8f} second(s)")

"""
    1. Strip non-word characters
    2. Separate Strings by space
    3. If string length is greater than 4 run abbreviate fx
    4. Run the main function
    5. All non-word characters remain in place,
       all strings length less than 4 is kept as is.
"""
