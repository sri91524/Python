"""
closure is a technique which allows the storing of values in spite of the fact that the context in which they have been created does not exist anymore.
"""
def outer(par):
    loc = par
 
 
var = 1
outer(var)
 
# print(par)
# print(loc)
 
# The last two lines will cause a NameError exception – neither par nor loc is accessible outside the function
#############################################
def outer(par):
    loc = par

    def inner():
        return loc
    return inner

var = 1
fun = outer(var)
print(fun())
############################################
def make_closure(par):
    loc = par

    def power(p):
        return p ** loc
    return power

fsqr = make_closure(2)
fcub = make_closure(3)

for i in range(5):
    print(i, fsqr(i), fcub(i))

###################################################
def replace_spaces(replacement='*'):
    def new_replacement(text):
        return text.replace(' ', replacement)
    return new_replacement
 
 
stars = replace_spaces()
print(stars("And Now for Something Completely Different"))