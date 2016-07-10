# Module 2
#
# 1. How do you assign a variable? How do you print a variable?
my_var = 22
print(my_var) # ==> 22
print "%s" % my_var # ==> 22
# 2. What is the syntax to create 
# list
my_list = [1, 2, 3]
# tuple
my_tup = (1, 2, 3)
# dictionary
my_dict = {"one": 1, "two": 2, "three": 3}
# set
my_set = set([1, 2, 3])
# 3. How do you check for the existence of an element in 
# list
2 in my_list 
# tuple
2 in my_tup
# dictionary
'two' in my_dict
2 in my_dict.values()
'two' in my_dict.keys()
# set
2 in my_set
# 4. How do you create
# the union of a list
my_list2 = [3, 4, 5, 6]
list(set(my_list) | set(my_list2)) # ==> [1, 2, 3, 4, 5, 6]
# the intersection of a list
list(set(my_list) & set(my_list2)) # ==> [3]
# 5. What is the code to swap two variables?
my_var2 = 23
tmp = my_var
my_var = my_var2
my_var2 = tmp
print "my_var=",my_var,", my_var2=",my_var2 
# 6. How do you reverse a list?
my_list.reverse() # ==> [3, 2, 1] :method to reverse list
my_list[::-1] # prints list reversed
# 7. How do you create a list of integers
x = 11
# 0.....x
list(range(x+1)) # ==> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# 5.....x
list(range(5, x+1)) # ==> [5, 6, 7, 8, 9, 10, 11]
# 5,7,..x
list(range(5, x+1, 2)) # ==> [5, 7, 9, 11]
# 8. How do you obtain the last but one element of a list
my_list[-1] # ==> 3
# 9. Can you apply list commands to strings?
my_str = "some string"
list(my_str)
len(my_str)
max(my_str)
min(my_str) 

