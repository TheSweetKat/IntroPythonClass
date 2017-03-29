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

#Open the file created in the first script for read/write access
my_path = my_path = "c:\\temp\\mypythonfiles\\plague_warning.txt"
my_file = open(my_path, "r+")

#Create a for loop to print the contents of the file to the screen
for line in my_file:
    print(line)

#Go to Wikipedia to obtain a 3 sentence definition for the Black Plague
#Write the definition to the file
my_file.write("The Black Death was one of the most devastating pandemics in human history.\n")
my_file.write("Analysis of DNA from victims... indicates that the pathogen responsible was the Yersinia pestis bacterium.\n")
my_file.write("The world population as a whole did not recover to pre-plague levels until the 17th century.\n")
               

#Close the file
my_file.close()

#Reopen the file for reading
my_file = open(my_path, "r")

#Create a for loop to print the contents of the file to the screen
for line in my_file:
    print(line)

#Close the file
my_file.close()

print()
print()
input("Press enter key to continue ...")
# end of script
