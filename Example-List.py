# numbers = [10,5,7,2,1]
# print("Original list content:", numbers)

# numbers[0] = 111
# print("Previous list content", numbers)

# numbers[1] = numbers[4]
# print("New list contents:", numbers)
# print("List length:", len(numbers))

# del numbers[1] #Removing the second element from the list
# print("New list length", len(numbers))
# print("New list content", numbers)
# print(numbers[-1]) #last element in the list
# print(numbers[-2])
# print(numbers[-4])

"""
write a line of code that prompts the user to replace the middle number in the list with an integer number entered by the user (Step 1)
write a line of code that removes the last element from the list (Step 2)
write a line of code that prints the length of the existing list (Step 3).
"""
# number = [1, 2, 3, 4, 5]
# num = int(input("Enter number to replace middle number in 1,2,3,4,5: "))
# number[2] = num
# del number[4]
# print(len(number))
# print(number)

###
print("===============================================")
# numbers.append(4)
# print(numbers)
# print("Length of numbers: ", len(numbers))
# numbers.insert(0, 222)
# print(numbers)
# print(len(numbers))
# numbers.insert(1,333)
# print(numbers)

###
# my_list = []
# for i in range(5):
#     # my_list.append(i+1)
#     my_list.insert(0, i+1)
# print(my_list)

###
my_list = [10, 1, 8, 3, 5]
total = 0
# for i in range(len(my_list)):
#     total += my_list[i]
# print(total)

#In a handy way
for i in my_list:
    total += i
print(total)

#Swap the list to reverse the order
my_list = [10, 1, 8, 3, 5]
# my_list[0], my_list[4] = my_list[4], my_list[0]
# my_list[1], my_list[3] = my_list[3], my_list[1]
# print(my_list)

#swap the list to reverse the order with for loop to automate
# length = len(my_list)
# for i in range(length // 2):
#     my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

# print(my_list)

"""
step 1: create an empty list named beatles;
step 2: use the append() method to add the following members of the band to the list: John Lennon, Paul McCartney, and George Harrison;
step 3: use the for loop and the append() method to prompt the user to add the following members of the band to the list: Stu Sutcliffe, and Pete Best;
step 4: use the del instruction to remove Stu Sutcliffe and Pete Best from the list;
step 5: use the insert() method to add Ringo Starr to the beginning of the list.
"""
# beatles = []
# print("Step 1: ", beatles)

# beatles.append("John Lennon")
# beatles.append("Paul McCartney")
# beatles.append("George Harrison")
# print("Step 2: ", beatles)

# for i in range(2):
#     members = input("Enter members of the band: ")
#     beatles.append(members)
# print("Step 3: ", beatles)

# del beatles[-1]
# del beatles[-1] 
# print("Step 4: ", beatles)

# beatles.insert(0, "Ringo Starr")
# print("Step 5: ", beatles)

######################
# Example of nested list
my_list = [1, 'a', ["list", 64, [0, 1], False]]

##########################
"""
Increasing order -- Sort the list (bubble sort)
set swapped variable to True
then iterate, we'll take the first and the second elements and compare them; if we determine that they're in the wrong order (i.e., the first is greater than the second), we'll swap them round; if their order is valid, we'll do nothing.
then second and third until prior to last element
We create a variable named swapped, and we assign a value of False to it, to indicate that there are no swaps. Otherwise, it will be assigned True

"""
# my_list = [8, 10, 6, 2, 4]  # list to sort
# swapped = True
# while swapped:
#     swapped = False
#     for i in range(len(my_list)-1):
#         if(my_list[i] > my_list[i+1]):
#             swapped = True
#             my_list[i], my_list[i+1] = my_list[i+1], my_list[i] #to sort
# print(my_list)

print("====================================================")
# Sorting in Interactive session
# my_list = []
# swapped = True
# num = int(input("How many elements do you want to sort: "))
# for i in range(num):
#     val = float(input("Enter a list element: "))
#     my_list.append(val)

# while swapped:
#     swapped = False
#     for i in range(len(my_list)-1):
#         if my_list[i] > my_list[i+1]:
#             swapped = True
#             my_list[i], my_list[i+1] = my_list[i+1], my_list[i]

# print("Sorted", my_list)
print("=====================================================")
#Python method - sort
# my_list = [8, 10, 6, 2, 4]
# my_list.sort()
# print(my_list)
# my_list.reverse()
# print(my_list)

####
# It will copy list_1 name to list_2. so if there is any change in list_1 content, will affect list_2
list_1 = [1]
list_2 = list_1
list_1[0] = 2
print(list_2)

# Slice operator : it will copy content of list_1 to list_2
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)

my_list = [10, 8, 6, 4, 2]
# new_list = my_list[1:3] #end = end-1
# print(new_list)

# my_list = [10, 8, 6, 4, 2]
# new_list = my_list[1:-1]
# print(new_list)
# new_list = my_list[:3]
# print(new_list)
# new_list = my_list[3:]
# print(new_list)
# new_list = my_list[:]
# print(new_list)
# del my_list[1:3]
# print(my_list)
# del my_list[:]
# print(my_list)

#####
# in and not in operator
my_list = [0, 3, 12, 8, 2]
print(5 in my_list)
print(12 in my_list)
print(5 not in my_list)


#####
# largest number
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in range(1, len(my_list)):
    if my_list[i] > largest:
        largest = my_list[i]

print(largest)

#####
# largest number with slice
# my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
# largest = my_list[0]

# for i in my_list[1:]:
#     if i > largest:
#         largest = i

# print(largest)

# let's find the location of a given element inside a list:
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# to_find = 10
# found = False
# for i in my_list:
#     found = i == to_find
#     if found:
#         break
# if found:
#     print("Found the number in index ", i)
# else:
#     print("Number not found")


# you've chosen the following numbers in the lottery: 3, 7, 11, 42, 34, 49.
# The numbers that have been drawn are: 5, 11, 9, 42, 3, 49.
# num_list = []
# drawn = [5, 11, 9, 42, 3, 49]
# bets = [3, 7, 11, 42, 34, 49]
# hits = 0
# for number in bets:
#     if number in drawn:
#         num_list.append(number)
#         hits += 1

# print(num_list)
# print(hits)

"""
 Program which removes all the number repetitions from the list. The goal is to have a list in which all the numbers appear not more than once.
"""
# my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
num = int(input("Enter how many numbers do you want to enter to make unique list:"))
my_list = []

for i in range(num):
    val = input("Enter values to find unique: ")
    if val != "":
        my_list.append(int(val)) 

my_list = set(my_list)
print(my_list)

list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2
 
del list_1[0]
del list_2
 
print(list_3)
