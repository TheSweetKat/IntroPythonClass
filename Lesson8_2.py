# ---------------------------------------------------------
# Change Log
# Author    Date:       Change:             Reason:
# kzsweet    02/10/2016  Create Python Script  
#
# ---------------------------------------------------------
# Lesson8_2
# For Instructor: Lori Kelley Rodas
# Author: Kat Sweet
# 
# ---------------------------------------------------------
#
# insert Python Script after this comment

# storing addresses from command line prompts
address1 = input("First address: ")
address2 = input("Second address: ")

# comparing whether the two addresses match
if(address1 == address2):
    print("The addresses are EQUAL")
else:
    print("The addresses are NOT EQUAL")
    state = input("State for second address: ")
    zipcode = input("Zipcode for second address: ")
    print("Street:", address2)
    print("State:", state)
    print("Zipcode:", zipcode)


print()
print()
input("Press enter key to continue ...")
# end of script
