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

#Use the os module  and an if statement to determine if a directory
#exists and create a directory called c:\temp\mypythonfiles as needed
my_directory = os.path.isdir("c:\\temp\\mypythonfiles")
if(my_directory == False):
    os.system("md c:\\temp\\mypythonfiles")
    print("creating a new directory")


#Create a file called plague_warning.txt in the directory that was just created
my_path = "c:\\temp\\mypythonfiles\\plague_warning.txt"
my_file = open(my_path, "w")

    
#Write the text for the children's rhyme "Ring around the Rosie" to the
#file in multiple lines

my_file.write("Ring around the rosies\n")
my_file.write("A pocket full of posies\n")
my_file.write("Ashes, ashes\n")
my_file.write("We all fall down.\n")

#Close the file
my_file.close()
                 
print()
print()
input("Press enter key to continue ...")
# end of script
