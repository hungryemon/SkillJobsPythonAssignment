# 2. Write a Python program to find the
# first appearance of the substring 'not' and 'poor'
# from a given string,
# if 'not' follows the 'poor',
# replace the whole 'not'...'poor' substring with 'good'.
# Return the resulting string. Go to the editor
# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'

# Defining function to change input string
def change_str(inputStr):

    # Making string lowercase in case of uppercase inputs and finding 'not' and poor'
    snotindex = inputStr.lower().find('not')
    spoorindex = inputStr.lower().find('poor')

    # Checking they exists in string and 'poor' is after 'not'
    if spoorindex > snotindex >= 0:
        expectedstr = inputStr.replace(inputStr[snotindex:(spoorindex + 4)], 'good')  # Replacing 'not ... 'poor' with 'good
        print(expectedstr)
    else:
        print(inputStr)


inputStr = input("Enter the String: ")
change_str(inputStr)
