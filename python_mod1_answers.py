# Module 1
# 
# What are the three basic rules for code annotation?
# >> 
'''1. Give a meaningful names for a variables and functions.
2. Write brief comments explaining the reasons behind particularly
important or complex statements.
3. Add docstrings to own functions/methods/classes and modules.'''
# 1. Which python version is installed on your system (type python in a terminal)
# >> Python 2.7.6
# 2. How do you print a string/numeric?
my_string = "mystring"
print(my_string) # ==> mystring
print("mystring") # ==> mystring
my_num = 3
print(my_num) # ==> 3
# 3. What is the effect of using “+” to add strings? What is the difference between “2”+”2” and 2+2
"2"+"2" # ==> '22'
2+2 # ==> 4
# 4. How can you add a number and a string?
my_string + str(my_num) # ==> 'mystring3'
# 5. What is the result of 1 / 2 and why?
1/2 # ==> 0 by default python performs integer division
# 6. How can you print inverted commas?
print "’" # ==> ’
print '’' # ==> ’
# 7. Are following expression True/False and why? 
False==0 # ==> True
2>False  # ==> True :False equal to 0 
True==0  # ==> False :True equal to 1
True==2  # ==> False :True equal to 1
"2"==2   # ==> False :"2" and 2 have different types 
"2"=='2' # ==> True :"2" and '2' both have type strings 
"'"=='\''# ==> True :'\' used here for escaping a character
# 8. How do you extract the first letter of a string?
"How do you extract the first letter of a string?"[0] # ==> 'H'
# 9. How do you extract the second digit of a numeric variable?
my_num2 = 321
str(my_num2)[1] # ==> '2'


