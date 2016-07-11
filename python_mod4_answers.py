# Module 4
#
'''1. Write a function that returns the GC content of a string(e.g. a DNA string that 
contains of the four letters A,C,G,T or a,c,g,t)'''
seq = 'gtgggcctcaaatgtggagcactattctgatgtccaagtggaaagtgctgcgacatttgagcgtcac'.upper()
def gc_content(my_data):
    counts = {'A':0, 'T':0, 'G':0, 'C':0}
    for base in my_data:
	counts[base] += 1
    return (counts['G'] + counts['C']) / float(len(my_data)) * 100
# 2. Do you need to return a value in a function?
# >> not always, by default function will return None without 'return'
# 3. What is the “None” object
# >> is a Python object, denoting lack of value. It has no methods
# 4. Write a recursive function (a function that calls itself) to calculate faculty.
st_list = {"Anna": "chemical", "Anastasia": "physical", "Andrew": "mathematical"}
def faculty():
    global st_list
    student = str(raw_input("Please enter the student's name:\n"))
    try:
	print student, "faculty is \n", st_list[student] 
    except KeyError:
	print student, "is not in the list"
    faculty()
# 5. Can you overload functions (use the same function name with different input parameters) in Python?
# >> in Python functions can not be overloaded, though there are some tricks to avoid it.
# 6. What is the difference between a global and local variable? How can you define a global variable in a local context?
''' >> local variables can be accessed only inside the function in which
they are declared, whereas global variables can be accessed throughout 
the program body by all functions. Global variable could be defined inside the 
function for example using reserved word 'global' '''
