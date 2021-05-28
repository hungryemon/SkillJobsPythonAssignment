# 4. Write a Python program to remove duplicates from a list.

lst = []
n = int(input("Enter number of elements : "))

for i in range(0, n):
    ele = input()
    lst.append(ele)  # Adding the element


# # Using POP() *** Doesn't remove all duplicates ***
# for i in lst:
#     if lst.count(i) > 1:
#         ind = lst.index(i)
#         lst.pop(ind)
# print(lst)

# Using Set()
newLst = list(set(lst))  # As Set does not include duplicate values
print(newLst)
