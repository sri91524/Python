"""
    write a function able to input integer values and to check if they are within a specified range.

    The function should:

    accept three arguments: a prompt, a low acceptable limit, and a high acceptable limit;
    if the user enters a string that is not an integer value, the function should emit the message Error: wrong input, and ask the user to input the value again;
    if the user enters a number which falls outside the specified range, the function should emit the message Error: the value is not within permitted range (min..max) and ask the user to input the value again;
    if the input value is valid, return it as a result.
"""
def validateNumber(prompt, LAL, HAL):  
    while True:
        try:
            val = int(input(prompt))          
            if not LAL <= val <= HAL:
                print(f"Error: the value is not with permitted range ({LAL}..{HAL})")
            else:
                return val
        except ValueError:
            print("Wrong Input")
    return val

result = validateNumber("Enter a number from -5 to 25: ", -5, 25)
print("The number is : ", result)