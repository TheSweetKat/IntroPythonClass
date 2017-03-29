# ---------------------------------------------------------
# Change Log
# Author    Date:       Change:             Reason:
# kzsweet    02/10/2016  Create Python Script  
#
# ---------------------------------------------------------
# Python Scripting Activity
# For Instructor: Lori Kelley Rodas
# Author: Kat Sweet
# 
# ---------------------------------------------------------
#
# insert Python Script after this comment

#importing the sys module
import sys

#the four arguments from the command line
my_name = sys.argv[1]
test1 = sys.argv[2]
test2 = sys.argv[3]
test3 = sys.argv[4]

test1 = int(test1)
test2 = int(test2)
test3 = int(test3)

#average of the three test scores
average = (test1 + test2 + test3) / 3

print("The test average for", my_name, "is", average)

# the pause before ending script
print()
print()
input("Press enter key to continue ...")
# end of script