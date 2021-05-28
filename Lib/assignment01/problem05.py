# 5. Write a Python function that takes two lists and
#   returns True if they have at least one common member.
lst1 = []
n = int(input("Enter number of elements for 1st: "))

for i in range(0, n):
    ele = input()
    lst1.append(ele)  # Adding the element

lst2 = []
n = int(input("Enter number of elements for 2nd list: "))

for i in range(0, n):
    ele = input()
    lst2.append(ele)  # Adding the element

print(lst1)
print(lst2)

lst1_as_set = set(lst1)
intersection = lst1_as_set.intersection(lst2)

# print(intersection)

if len(intersection) > 0:
    print(True)