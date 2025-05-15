def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)
 
introduction(first_name = "James", last_name = "Bond")
introduction(last_name = "Skywalker", first_name = "Luke")

# Positional Arguement
def subtra(a, b):
        print(a - b)

subtra(5, 2)
subtra(2, 5)

# Keyword arguement
def subtra(a, b):
      print(a - b)

subtra(a = 5, b = 2)
subtra(b = 2, a = 5)

# Mix arguement (position arguement placed before keyword arguement)
def subtra(a, b):
      print(a - b)

subtra(2, b = 5)

# default parameter
def name(first_name, last_name = "Smith"):
      print(first_name, last_name)

name("Andy")
name("Betty", "Johnson")
