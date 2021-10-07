'''
Prior to having fancy iPhones, teenagers would wear out their thumbs
sending SMS messages on candybar-shaped feature phones with 3x4 numeric keypads.
In order to send the message "WHERE DO U WANT 2 MEET L8R"
a teen would have to actually do 47 button presses. No wonder they abbreviated.

For this assignment, write a module that can calculate the amount of button presses
required for any phrase. Punctuation can be ignored for this exercise. Likewise,
you can assume the phone doesn't distinguish between upper/lowercase characters
(but you should allow your module to accept input in either for convenience).

Hint: While it wouldn't take too long to hard code the amount of key presses
for all 26 letters by hand, try to avoid doing so! (Imagine you work at a
phone manufacturer who might be testing out different keyboard layouts,
and you want to be able to test new ones rapidly.)

Notes
    * and # must be separate keys
'''

from timeit import default_timer as timer

start_time = timer()


def presses(phrase):
    key_dict = {'2': 'ABC2', '3': 'DEF3', '4': 'GHI4', '5': 'JKL5',
                '6': 'MNO6', '7': 'PQRS7', '8': 'TUV8', '9': 'WXYZ9',
                '0': ' 0', '*': '*', '#': '#', '1': '1'}

    answer = 0
    for char in phrase.upper():
        for keys, value in key_dict.items():
            if char in value:
                answer += (value.index(char) + 1)
            else:
                pass

    return answer


print(presses("HOW R U"))

end_time = timer()
total_time = end_time - start_time
print(f'Program took: {total_time:8f} seconds to complete')
