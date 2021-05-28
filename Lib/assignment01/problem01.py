# 1. Write a Python program to get a string made of the first 2 and
# the last 2 chars from a given a string.
# If the string length is less than 2,
# return instead of the empty string.
# Go to the editor:
# Sample String : 'assignment'
# Expected Result : 'asnt'
# Sample String : 'as'
# Expected Result : 'asas'
# Sample String : ' a'
# Expected Result : Empty String

inputStr = input("Enter a string: ")

# print(inputStr.strip())

# Check if the String length is less than 2 while removing front and end white spaces
if len(inputStr.strip()) < 2:
    print("Empty string")

else:
    str1 = inputStr[0:2]  # First 2 characters
    str2 = inputStr[-2:]  # Last 2 characters
    str3 = str1 + str2  # Joining First & Last 2 characters
    print(str3)
