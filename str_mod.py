import random
#
def conson(inp_str):
    new_string = ''
    consonants = set("bcdfghjklmnpqrstvwxyz")
    for char in inp_str.lower():
            if char in consonants:
                new_string += char
    print new_string
    return
#
def shuffle(inp_str):
    print ''.join(random.sample(inp_str, len(inp_str)))
    return
    

