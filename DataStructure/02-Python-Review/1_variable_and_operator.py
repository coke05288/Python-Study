# variable
number = 3

pi = 3.14  # float variable
comp = 2 + 2j  # complex variable
isvalid = True  # boolean variable
msg = "Reviewing Python"  # string variable
A = [0, 1, 2, 3, 4]  # list variable

print()

# arithmetic operators
number = (number + 3) * 4.0 / 2
print(number)  # 12.0

pi_div = pi / 2
print(pi_div)  # 1.57

pi_div = pi // 2
print(pi_div)  # 1.0

print()

# binary operators
number = 2
number = 2**3
print(number)  # 8

print()

# assignment operators
number = 2
number += 2
number -= 2
print(number)  # 2

print()


# boolean operators
avg = 83
if avg >= 80 and avg < 90:
    print("{}points is B Rate".format(avg))

print()

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1
print(list1 == list2)  # compare the value of the referenced object
print(list1 is list2)  # compare referenced object itself
print(list1 == list3)
print(list1 is list3)

print()

print(msg in 'R')
print(msg in "Reviev")

print()