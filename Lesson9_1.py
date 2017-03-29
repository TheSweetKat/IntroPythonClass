# ---------------------------------------------------------
# Change Log
# Author    Date:       Change:             Reason:
# kzsweet    02/16/2016  Create Python Script  
#
# ---------------------------------------------------------
# Lesson9_1
# For Instructor: Lori Kelley Rodas
# Author: Kat Sweet
# 
# ---------------------------------------------------------
#
# insert Python Script after this comment

# Remember to run this script with 3 command line arguments

# use the sys module to accept 3 command line arguments
import sys

num1 = sys.argv[1]
num2 = sys.argv[2]
num3 = sys.argv[3]

# cast the command line inputs as integers

num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

# compare the three numbers

if(num1 == num2 and num1 < num3):
    print("the first condition is TRUE")
if(num1 < num2 and num1 < num3):
    print("the second condition is TRUE")
if(num1 == num2 and num3 < num2):
    print("the third condition is TRUE")
if(num1 == num3 or num1 < num3):
    print("the fourth condition is TRUE")
if(num1 == num2 or num1 > num3):
    print("the fifth condition is TRUE")

# ending the script with a pause

print()
print()
input("Press any key to continue...")

# end of script
