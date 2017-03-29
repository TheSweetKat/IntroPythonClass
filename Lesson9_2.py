# ---------------------------------------------------------
# Change Log
# Author    Date:       Change:             Reason:
# kzsweet    02/16/2016  Create Python Script  
#
# ---------------------------------------------------------
# Lesson9_2
# For Instructor: Lori Kelley Rodas
# Author: Kat Sweet
# 
# ---------------------------------------------------------
#
# insert Python Script after this comment

# Remember to run this script with command line input

# use the sys module to accept a command line argument
import sys

num1 = sys.argv[1]

# cast the command line input as integer

num1 = int(num1)

# print condition based on the number

if(num1 < 12):
    print("the first condition is TRUE")
elif(num1 == 19):
    print("the second condition is TRUE")
elif(num1 > 19 and num1 < 31):
    print("the third condition is TRUE")
elif(num1 >= 42 and num1 < 100):
    print("the fourth condition is TRUE")
else:
    print("all conditions are FALSE")

# ending the script with a pause

print()
print()
input("Press any key to continue...")

# end of script
