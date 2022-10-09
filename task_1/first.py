import math
from random import randint

# Decimal expansion Formula = Sumatory of b*10^k
# link: https://www.cut-the-knot.org/arithmetic/BaseExpansion.shtml
# link: https://mathworld.wolfram.com/DecimalExpansion.html


def get_expansion(num):
    # split_values represent two lists, means split_values[0] and  split_values[1]
    # split_values[0] represent the integer part and split_values[1] represent all after .
    split_values = str(num).split('.')
    values = list(str(num))  # here converts the number to a list of values
    # to define the real len,  just needs the int part -1
    exp = len(split_values[0]) - 1
    expansion = 0

    for b in values:
        if b != '.':
            expansion += math.pow(int(b)*10, exp)
            # print(f'{b}*10^{exp} | resultado:{math.pow(int(b)*10, exp)}')
            exp -= 1
    # Return the decimal expansion  acording to the internet documentation
    return (expansion)


# Use zeroes_plus function for test get_expansion() function
def zeroes_plus(n):
    # here I get the real value of decimal expansion
    real_value = get_expansion(n)
    # here convert the real value to string and convert it in a list
    expansion = list(str(real_value))
    # Using .count('0') this will count all elements 0 into the list so zeroes(n) return numbers of 0 into the decimal expansion
    return (expansion.count('0'))


def zeroes(n):
    # here convert the real value to string and convert it in a list
    expansion = list(str(n))
    # Using .count('0') this will count all elements 0 into the list so zeroes(n) return numbers of 0 into the number
    return (expansion.count('0'))


# Check if number is zero special or not.
# this funtion return true is zero_special else return false
def zero_special(n):
    if zeroes(n) > zeroes(n-1):
        return True
    return False


'''
Nota : test_zero_special is a recursive function just for test some random numbers 
The following part contains a function just to do a test to zero_special
here just I use the magic of recursion, jejejejeje
'''


def test_zero_special(n, accumulated_number):

    if n >= 300:
        return accumulated_number

    else:
        if zero_special(n):
            print(f'value: {n}, is zero_special...')
        else:
            print(f'value: {n}, is not zero_special...')

        rdn = randint(100, 200)

        return test_zero_special(n + rdn, accumulated_number + n)


# Calling the recursive function for a test
# test_zero_special function need to start with two initial values
test_zero_special(100, 0)
