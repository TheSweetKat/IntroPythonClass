# ---------------------------------------------------------
# Change Log
# Author    Date:       Change:             Reason:
# UserID    02/15/2016  Create Python Script  
#
# ---------------------------------------------------------
# Lesson8_1
# For Instructor: Lori Kelley Rodas
# Author: Kat Sweet
# 
# ---------------------------------------------------------
#
# insert Python Script after this comment

import sys

# assigning the command-line input to variables
num1 = sys.argv[1]
num2 = sys.argv[2]

# changing the variables' data types to integers
num1 = int(num1)
num2 = int(num2)

# comparing whether the two numbers are equal
if(num1 == num2):
    print("the numbers are EQUAL")
    print()
else:
    print("the numbers are NOT EQUAL")
    print()

# print if the first number is less than the second
if(num1 < num2):
    print("the first number is LESS")

# print if the second number is less than the first
if(num2 < num1):
    print("the second number is LESS")

print()
print()
input("Press enter key to continue ...")
# end of script
