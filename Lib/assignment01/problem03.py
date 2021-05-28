# 3. Write a Python program to get the largest number from a list.


# creating an empty list
lst = []

# number of elemetns as input
n = int(input("Enter number of elements : "))

# iterating till the range
for i in range(0, n):
    ele = int(input())  # Working with only integer values in list(no float/string)

    lst.append(ele)  # adding the element

print(lst)

lrgNum = (max(lst))  # finding Largest number

print("Largest number:", lrgNum)
