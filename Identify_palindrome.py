# Requirement #1 – Identify palindrome:

# Create a Python function that takes a list of at least 2 elements and returns “True” if the 
# list is a palindrome and “False” if it isn’t. 

# Underneath the function code, write some Python test code to test your function.

# Use the following data to create a Python nested list which you can loop through, 
# extracting each sub list and invoking your function. 

# 1, 2, 3, 5, 7, 7, 0 
# “Red”, “Green”, “Blue” 
# 1, 0, 0, 1, 0, 0, 1 
# “Red”, “Yellow”, “Green”, “Yellow”, “Red” 

# As you extract each sub list, and test to see if it’s a palindrome, print out to the console, 
# the original sub list and the palindrome test result. 

# Creates the sublists and the nested list:
list = [] # Creates a empty list called "list" - this will be the nested list.
revsl = []

# Creates the sublists:
sl1 = [1, 2, 3, 5, 7, 7, 0]
sl2 = ["Red", "Green", "Blue"]
sl3 = [1, 0, 0, 1, 0, 0, 1 ]
sl4 = ["Red", "Yellow", "Green", "Yellow", "Red"]

# Creates the nested list:
list = [sl1, sl2, sl3, sl4]

# STEP 02 - COMPARE THE ITEMS OF THE LIST TO IDENTIFY IF IT IS A PALINDROME (FIRST = LAST?; SECOND = SECOND LAST?;...)
n = len(list)
for i in range(0, n):
    subl = list[i]
    revsubl = subl[::-1]
    pali = subl == revsubl
    print(str(subl) + " " + str(pali))

# END OF REQUIREMENT #1
###########################################################################################################################################

# Requirement #2 – Multiply two matrices element by element

# Create a Python function that takes two nested lists as parameters and returns a single nested list that is the product of the two input lists. 
# In this case, calculating the product means multiplying each numeric element in the first nested list (matrix) by each corresponding element 
# in the second nested list and placing the result in the corresponding element in the third nested list. 

# Creating the nested input lists that will the multiplied.
nlist1 = [[1, 2, 3, 5, 7, -7, 0], [112, 43, 17, 6, 2, 118, 11], [1024, 512, 256, 128, 64, 32, 16]]
nlist2 = [[9, 81, 75, 42, 5, -113, -1], [11, 2, -3, 0, 7, 0, 9], [8, 6, 2, 1, 0, -1, -2]]

# Creating the lists that will store the partial result and the final result.
nlist3 = [] # Partial result.
nlist4 = [] # Final result list.

n = len(nlist1)
nn = len(nlist1[0])

for i in range(0, n):
    for j in range(0, nn):
        nlist3.append(nlist1[i][j] * nlist2[i][j])
    nlist4.append(nlist3)
    nlist3 = []
print(nlist4)

# END OF REQUIREMENT #2
###########################################################################################################################################

# Requirement #3 – Multiply single list vector to produce a single scalar

# As a follow up from Requirement #2, create a new function that takes a single list 
# parameter (not a nested list) and multiples all the integer values together and then 
# returns the calculated number (scalar).

# Creating the input list:
list3 = [1024, 512, 256, 128, 64, 32, 16]
n3 = len(list3)
x = 1 # Var'x' will hold the final value.

# Multiplication loop:
for i in range(0, n3):
    x = x * list3[i]
print(x)

# END OF REQUIREMENT #3
###########################################################################################################################################