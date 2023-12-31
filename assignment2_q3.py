"""
NAME:      Danh Tran Hong
Student_ID:100403435
"""


# Define a function to calculate power by input 2 variables base & exp, the result will return result
# Checking even/odd by Modulus operator, if  exp % 2 == 0 , it means is even numbers, else it is odd numbers 
# Then power is calculated by formulation.
# Calulate by  (exp//= 2), to get result in integeter type

def compute_power(base, exp):
    result = 1

    while exp > 0:          #  For example, with exp = 3 
        if exp % 2 == 1:    # Check exp is odd or even
            result *= base  #  If exp is odd we calculate  result = result * base ( result = 1 * 2  => result = 2 )
        base *= base        # Then calculate base = base * base =>  base = 2 * 2  base *=base  <=>  base = base * base => base = 2 * 2 (4)   => base = 4
        exp //= 2           # exp = 3 // 2   ( exp = 1)
                            # Finish the first loop.  
                            # exp = 1 > 0 => keep running the loop
                            # reslut = result * base  = 2 * 4 = 8
                            # base = base * base  =  4 * 4 
                            # exp = exp // 2  = 1   => exp = 1  => odd number => result = result * base => result = 1 * 8
    return result           # return result value.
# Print for testing 
print(compute_power(2,3)) 

# make a list with name "powers" by using  function compute_power(2,x), and x variable which is generated by iteration control.
# Print the list "powers"
powers = [ compute_power(2,x) for x in range (0 ,10**3) ]
print(powers)
