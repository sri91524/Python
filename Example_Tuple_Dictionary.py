## tuple - sequence type and immutable

# my_tuple = (1, 10, 100, 1000)
# print(my_tuple[0])
# print(my_tuple[-1])
# print(my_tuple[1:])
# print(my_tuple[:-2])

"""
don't try to modify a tuple's contents! It's not a list!
immutable
All of these instructions (except the topmost one) will cause a runtime error:
my_tuple = (1, 10, 100, 1000) 
my_tuple.append(10000)
del my_tuple[0]
my_tuple[1] = -10
"""
#######################################
my_tuple = (1, 10, 100)

# t1= my_tuple + (1000, 10000)
# t2 = my_tuple * 3
# print(len(t2))
# print(t1)
# print(t2)
# print(10 in my_tuple)
# print(-10 not in my_tuple)

##########################################
var = 123
t1 = (1, )
t2 = (2, )
t3 = (3, var)
t1, t2, t3 = t2, t3, t1

print(t1, t2, t3)
###########################################
## Dictionary
dictionary = {"cat":"chat", "dog": "chien", "horse" : "cheval"}
phone_numbers = {'boss': 5551234567, 'Suzy':22657854310}
empty_dictionary = {}
print(dictionary)
print(dictionary['cat'])
print(phone_numbers['Suzy'])
print(empty_dictionary)

# in operator
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"} # tuple
words = ['cat', 'lion', 'horse'] # list
for word in words:
    if word in dictionary:
        print(word, "->",dictionary[word])
    else:
        print(word, " is not in dictionary")

# vertically aligned
# Example 1:
dictionary = {
              "cat": "chat",
              "dog": "chien",
              "horse": "cheval"
}
# Example 2:
phone_numbers = {'boss': 5551234567,
              'Suzy': 22657854310
}
####################################
# iterating keys
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
for key in dictionary.keys():
    print(key, "->", dictionary[key])

# iterating items will return tuple (key, value pair)

for english, french in dictionary.items():
    print(english, "->", french)

# modifyint a value
dictionary["cat"] = "minou"
print(dictionary)

# for key in sorted(dictionary.keys()):
for french in dictionary.values():
    print(french)

###################################
# add a new key
dictionary["swan"] = "cygne"
print(dictionary)

dictionary.update({"duck":"canard"})
print(dictionary)

del dictionary["dog"]
print(dictionary)

dictionary.popitem()
print(dictionary)

"""
you need a program to evaluate the students' average scores;
the program should ask for the student's name, followed by her/his single score;
the names may be entered in any order;
entering an empty name finishes the inputting of the data (note 1: entering an empty score will raise the ValueError exception, but don't worry about that now, you'll see how to handle such cases when we talk about exceptions in the second part of the Python Essentials course series)
a list of all names, together with the evaluated average score, should be then emitted.
"""
# school_class = {}

# while True:
#     name = input("Enter the student's name: ")
#     if name == '':
#         break
#     score = int(input("Enter the student score(0-10): "))
#     if score not in range(0,11):
#         break

#     if name in school_class:
#         school_class[name] += (score, )
#     else:
#         school_class[name] = (score, )

#     for name in sorted(school_class.keys()):
#         adding = 0
#         counting = 0
#         for score in school_class[name]:
#             adding += score
#             counting += 1
#         print(name, ":", adding/counting)
####################################################
my_tuple = (1, 2, True, "a string", (3, 4), [5, 6], None)
print(my_tuple)
 
my_list = [1, 2, True, "a string", (3, 4), [5, 6], None]
print(my_list)

# one-element tuple 
one_elem_tuple_1 = ("one", ) # Brackets and a comma.
one_elem_tuple_2 = "one",

# can access tuple elements by indexing them
my_tuple = (1, 2.0, "string", [3, 4], (5, ), True)
print(my_tuple[3])

# cannot append tuples, or modify, or remove tuple elements
my_tuple = (1, 2.0, "string", [3, 4], (5, ), True)
my_tuple[2] = "guitar" # The TypeError exception will be raised.

# delete a tuple as a whole
my_tuple = 1, 2, 3,
del my_tuple
print(my_tuple)

#Python built-in function called tuple(). when you want to convert a certain iterable (e.g., a list, range, string, etc.) to a tuple
my_list = [2, 4, 6]
print(my_list) # outputs: [2, 4, 6]
print(type(my_list)) # outputs: <class 'list'>
tup = tuple(my_list)
print(tup) # outputs: (2, 4, 6)
print(type(tup))

# convert an iterable to a list, you can use a Python built-in function called list():
tup = 1, 2, 3,
my_list = list(tup)
print(type(my_list)) # outputs: <class 'list'>

# clear() - dictionary - removes all item, del removes specific item
pol_eng_dictionary = {
    "zamek": "castle",
    "woda": "water",
    "gleba": "soil"
    }
pol_eng_dictionary.clear() # removes all the items

# To copy a dictionary, use the copy() method
copy_dictionary = pol_eng_dictionary.copy()

