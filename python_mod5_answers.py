# Module 5
#
# 1. How and where to import a module in a python script?
# >> modules customary imported at the beginning of a script using 'import' statement
# 2. Check if following modules are installed on your computer and import them: scipy, numpy, rpy, math
# 3. How can you check what functions and attributes are included in a module?
# >> dir(math)
# 4. Create your own module with two functions and import it to a separate script to run the functions.
# >> str_mod.py:
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
#
import str_mod
my_str = "Hello world!"
str_mod.conson(my_str) # ==> hllwrld
str_mod.shuffle(my_str) # ==> ool!rdH lelw

