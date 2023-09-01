"""
NAME:      Danh Tran Hong
Student_ID:100403435
"""

# Define a function to calculate power by input 2 variables base & exp, the result will return result

def compute_power(base, exp):
    if exp == 0:
        return 1
    elif exp < 0:
        return 1/compute_power(base, -exp)
    else:
        return base * compute_power(base, exp - 1)

# make a list with name "powers" by using  function compute_power(2,x), and x variable which is generated by iteration control.
# Print the list "powers",

powers = [ compute_power(2,x) for x in range (0 ,10**2) ]
print(powers)

# The function doesn't run succesfully, and it shows the error output as below: 

#  File "D:\Data_Analytics\CPSC4800\Assignment2_Q2.py", line 10, in compute_power
#     return base * compute_power(base, exp - 1)
#                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   [Previous line repeated 995 more times]
# RecursionError: maximum recursion depth exceeded
# Explain: 
# Because sys.getrecursionlimit() function has recursuion maximum value.
# It returns the current value of the recursion limit, the maximum depth of the Python interpreter stack. 
# So when I run the code with range (0, 10**3), the recursion will overload, while 10**2  is successful. 