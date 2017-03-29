# ---------------------------------------------------------
# Change Log
# Author    Date:       Change:             Reason:
# kzsweet   05/04/2016  Create Python Script  
#
# ---------------------------------------------------------
# Python Scripting Activity
# For Instructor: Lori Kelley Rodas
# Author: Kat Sweet
# 
# ---------------------------------------------------------
#
# insert Python Script after this comment

import os

#Use the os module to execute dir \s c:\windows\system32 while redirecting
#to a file called c:\temp\mypythonfiles\dirout.txt

my_path = "dir \\s c:\\windows\\system32"
my_script = "c:\\temp\mypythonfiles\\dirout.txt"
my_command = my_path + " > " + my_script
os.system(my_command)


#Open the file dirout.txt for reading
my_file = open(my_script, "r")


#Create a loop to print the contents to the screen

for line in my_file:
    print(line)

#Close the file
my_file.close()



print()
print()
input("Press enter key to continue ...")
# end of script
