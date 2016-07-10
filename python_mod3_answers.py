# Module 3
#
# 1. How to use the ”for … in” loop to extract every other letter of a string
my_str = "This is some string"
for letter in my_str:
    print(letter)
# 2. Use the “if ... elif … else” function to check if a variable contains letters, numerics or both
my_var = "abc"
if any(c.isalpha() for c in my_var) and not any(c.isdigit() for c in my_var):
    print "my_var contains letters"
elif not any(c.isalpha() for c in my_var) and any(c.isdigit() for c in my_var):
    print "my_var contains digits"
elif any(c.isalpha() for c in my_var) and any(c.isdigit() for c in my_var):
    print "my_var contains letters and digits"
else:
    print "my_var does not contain letters or digits"
# ==> my_var contains letters
# 3. Use the “for … in” loop to calculate faculty
st_list = {"Anna": "chemical", "Anastasia": "physical", "Andrew": "mathematical"}
for student in st_list.keys():
    print student, "faculty is ", st_list[student]
# 4. Use the “while … ” loop to calculate faculty
i = 0
while i < len(st_list):
    print st_list.keys()[i], "faculty is ", st_list.values()[i]
    i += 1
# 5. Use a suitable loop to check if a number is a prime number
my_var = 3
if my_var % 2 == 0:
    print my_var, "is a prime number"
# 6. Use a suitable loop to check if a number is a prime number
import math
my_num = 24
is_prime = True
for i in range(2, int(math.sqrt(my_num))):
    if my_num % i == 0:
	print my_num, "is not a prime number"
	is_prime = False
	break
    else:
	i += 1
if is_prime == 1:
    print my_num, "is a prime number"
# 7. Code an exception handling for a zero division
for i in range(-5,5):
    try:
        print(1.0 / i)
    except ZeroDivisionError:
        print "Division by zero error occured!"
# 8. Assume a string of coding DNA, extract for each letter the codon position (1st,2nd and 3rd) using a loop and the if command
seq = 'gtgggcctcaaatgtggagcactattctgatgtccaagtggaaagtgctgcgacatttgagcgtcac'.upper()
codontable = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }
for n in range(0,len(seq),3):
    if seq[n:n+3] in codontable:
	letter = codontable[seq[n:n+3]]
	print letter, seq[n:n+3], n, n+1, n+2




    

