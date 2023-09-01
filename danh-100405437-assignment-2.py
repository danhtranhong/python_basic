def compute_power(base, exp):
    if exp == 0:
        return 1
    elif exp < 0:
        return 1/compute_power(base, -exp)
    else:
        return base * compute_power(base, exp - 1)

# test  = compute_power(2,-3)
# print(test)
# # # Output: 32


powers = [ compute_power(2,x) for x in range (0 ,10**3) ]
print(powers)