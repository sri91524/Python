# Digit of life
"""
# asks the user her/his birthday (in the format YYYYMMDD, or YYYYDDMM, or MMDDYYYY – actually, the order of the digits doesn't matter)
# outputs the Digit of Life for the date.
"""
bdate = input("Enter birthday (in the format YYYYMMDD, or YYYYDDMM, or MMDDYYYY) : ")
try: 
    if not bdate.isdigit():
        print("Invalid Input")
    else:
        digit_sum = sum(int(num) for num in bdate)
        while digit_sum > 9:
            digit_sum = sum(int(num) for num in str(digit_sum)) 
    print("Digit of life is - ", digit_sum)
except:
    print("Invalid Input")