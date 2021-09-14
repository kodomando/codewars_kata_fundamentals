def encode(st):
    string = ''
    codes = {'a':'1', 'e':'2', 'i':'3', 'o':'4', 'u':'5'}
    for char in st:
        if char in codes.keys():
            string += codes[char]
        else:
            string += char
    return string

def decode(st):
    string = ''
    codes = {'1':'a', '2':'e', '3':'i', '4':'o', '5':'u'}
    for char in st:
        if char in codes.keys():
            string += codes[char]
        else:
            string += char
    return string