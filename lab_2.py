#!/bin/python

'''
Lab instructions: 
Complete each function below so that all doctests pass.
Recall that you can run the doctests by running the command
$ python3 -m doctest --verbose lab.py
Once all doctests pass, upload the output of the above command to sakai.
NOTE:
Each problem should be relatively straightforward and take less than 10 minutes.
If you're spending more than 10 minutes on a problem,
then you should stop and seek help.
NOTE:
Your grade for all labs will be equal to max(0, 5 - number of failing test cases)
'''

import math
def hypotenuse(a, b):
    result = (math.sqrt(a**2+b**2))
    return result
    '''
    Return the square root of a squared plus b squared.
    >>> hypotenuse(3.0, 4.0)
    5.0
    >>> hypotenuse(12.0, 5.0)
    13.0
    '''
print (hypotenuse(3.0,4.0))
print (hypotenuse(12.0,5.0))
print("-------------------------------")


def is_even(n):
    if n%2==0:
        return True
    else:
        return False
'''
    Return True if n is even and False if n is odd.
    HINT: Use the modulus operator %
    >>> is_even(0)
    True
    >>> is_even(1)
    False
    >>> is_even(2000)
    True
    >>> is_even(-8)
    True
    >>> is_even(-9)
    False
'''
print(is_even(0))
print(is_even(1))
print(is_even(2000))
print(is_even(-8))
print(is_even(-9))
print("-------------------------------")


def is_odd(n):
    if n%2==0:
        return False
    else:
        return True
    '''
    Return True if n is odd and False if n is even.
    >>> is_even(0)
    False
    >>> is_even(1)
    True 
    >>> is_even(2000)
    False
    >>> is_even(-8)
    False
    >>> is_even(-9)
    True
    '''
print(is_odd(0))
print(is_odd(1))
print(is_odd(2000))
print(is_odd(-8))
print(is_odd(-9))
print("-------------------------------")


def absolute_value(n):
    if n<0:
        n=-n
    return n
    '''
    Return the absolute value of n.
    HINT:
    Use an if statement.
    >>> absolute_value(5)
    5
    >>> absolute_value(-5)
    5
    >>> absolute_value(5.5)
    5.5
    >>> absolute_value(-5.5)
    5.5
    '''
print(absolute_value(5))
print(absolute_value(-5))
print(absolute_value(5.5))
print(absolute_value(-5.5))
print("-------------------------------")   


def max_num(a, b):
    if a>=b:
        return a
    else:
        return b
    '''
    Return the maximum of a and b.
    HINT:
    Use an if statement.
    >>> max_num(4, 5)
    5
    >>> max_num(5, 4)
    5
    >>> max_num(-4, -5)
    -4
    >>> max_num(4, 4)
    4
    '''
print(max_num(4,5))
print(max_num(5,4))
print(max_num(-4,-5))
print(max_num(4,4))
print("-------------------------------")


def max_num_4(a, b, c, d):
    if a>=b and a>=c and a>=d:
        return a
    elif b>=a and b>=c and b>=d:
        return b
    elif c>=a and c>=b and c>=d:
        return c
    else:
        return d
    '''
    Return the maximum of a, b, c, and d.
    HINT:
    Use many if statements.
    >>> max_num_4(1,2,3,4)
    4
    >>> max_num_4(2,3,4,1)
    4
    >>> max_num_4(3,4,1,2)
    4
    >>> max_num_4(4,1,2,3)
    4
    >>> max_num_4(10,1,2,3)
    10
    '''
print(max_num_4(1,2,3,4))
print(max_num_4(2,3,4,1))
print(max_num_4(3,4,1,2))
print(max_num_4(4,1,2,3))
print(max_num_4(10,1,2,3))
print("-------------------------------")


def max_num_abs(a, b):
    if a>=b and a<0 and b<0:
        return b

    if b>=a and a<0 and b<0:
        return a
    if a>=b and a>=0 and b>=0:
        return a
    if b>=a and a>=0 and b>=0:
        return b
    
    '''
    Return the number with the highest absolute value.
    HINT:
    Use an if statement, but be careful about the condition.
    >>> max_num_abs(4,5)
    5
    >>> max_num_abs(4,5)
    5
    >>> max_num_abs(-4,-5)
    -5
    >>> max_num_abs(4,4)
    4
    '''
print(max_num_abs(4,5))
print(max_num_abs(4,5))
print(max_num_abs(-4,-5))
print(max_num_abs(4,4))
print("-------------------------------")


def is_leap_year(n):
    if n%400 == 0:
        return True
    if n%100 == 0:
        return False
    if n%4 == 0:
        return True
    else:
        return False

    '''
    Return True if n is a leap year and False otherwise.
    HINT:
    You can find the formula to calculate leap years here at 
    https://www.mathsisfun.com/leap-years.html
    >>> is_leap_year(1582)
    False
    >>> is_leap_year(2000)
    True
    >>> is_leap_year(2018)
    False
    >>> is_leap_year(2019)
    False
    >>> is_leap_year(2020)
    True
    >>> is_leap_year(2200)
    False
    >>> is_leap_year(2400)
    True
    '''
print(is_leap_year(1582))
print(is_leap_year(2000))
print(is_leap_year(2018))
print(is_leap_year(2019))
print(is_leap_year(2020))
print(is_leap_year(2200))
print(is_leap_year(2400))
print("-------------------------------")


def num_digits(n):
    count = 0
    if n<0:
        n = -n
    if n==0:
        return 1
    while n>0:
        count+=1
        n//=10
    return count
        
'''
    Return the number of digits in the input n.
    NOTE:
    A negative sign does not count as a digit,
    only numbers do.
    HINT:
    Use a while loop.
    In each iteration, divide the number by 10 to reduce the number of digits by 1.
    >>> num_digits(5)
    1
    >>> num_digits(10)
    2
    >>> num_digits(45678)
    5
    >>> num_digits(123456789012345678901234567890)
    30
    >>> num_digits(-5)
    1
    >>> num_digits(-10)
    2
    '''
print(num_digits(5))
print(num_digits(10))
print(num_digits(45678))
print(num_digits(123456789012345678901234567890))
print(num_digits(-5))
print(num_digits(-10))
print("-------------------------------")

def factorial(n):
    a = 1
    for i in range (2,n+1):
       a = a*i
    return a
        
'''
    Return the factorial of n.
    Recall that the factorial of n is defined to be: 1*2*3*...*(n-1)*n 
    HINT: 
    Use a for loop from 1 to n.
    On each iteration, multiply the current result by the current iteration number.
    >>> factorial(1)
    1
    >>> factorial(2)
    2
    >>> factorial(3)
    6
    >>> factorial(4)
    24
    >>> factorial(10)
    3628800
    >>> factorial(100)
    93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
    '''
print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(4))
print(factorial(10))
print(factorial(100))
print("-------------------------------")

def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2,n):
        if (n % i) == 0:
            return False
    return True

    
    
print (is_prime(1))
print (is_prime(2))
print (is_prime(3))
print (is_prime(4))
print (is_prime(97))
print (is_prime(99))
print("-------------------------------")
            
'''
    Return True if n is prime, and False otherwise.
    Recall that a prime number is divisible only by itself and 1,
    and by convention 1 is not considered to be a prime number.
    HINT: 
    Use a for loop to check if every number between 2 and n-1 divides n
    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(4)
    False
    >>> is_prime(97)
    True
    >>> is_prime(99)
    False
'''


def is_perfect_square(n):
    for i in range(0,n+1):
        if n == i*i:
            return True
    return False
print(is_perfect_square(1))
print(is_perfect_square(2))
print(is_perfect_square(4))
print(is_perfect_square(81))
print(is_perfect_square(97))
print(is_perfect_square(0))
print(is_perfect_square(-144))
print(is_perfect_square(144))
print("-------------------------------")
    
    
'''
    Return True if n is is the product of two integers.
    That is, return True if there exists an integer i such that i*i==n.
    HINT: 
    Use a for loop to check each number i between 0 and n.
    >>> is_perfect_square(1)
    True
    >>> is_perfect_square(2)
    False
    >>> is_perfect_square(4)
    True
    >>> is_perfect_square(81)
    True
    >>> is_perfect_square(97)
    False
    >>> is_perfect_square(0)
    True
    >>> is_perfect_square(-144)
    False
    >>> is_perfect_square(144)
    True
    '''


def fibonacci(n):
    f0 = 0
    f1 = 1
    f2 = 1
    if n == 0:
        return f0
    if n == 1:
        return f1
    for i in range (2,n+1):
        f2= f0+f1
        f0=f1
        f1=f2
    return f2
print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))
print(fibonacci(6))
print(fibonacci(7))
print(fibonacci(1000))
print("-------------------------------")   


'''
    Return the nth fibonacci number.
    Recall that the fibonacci numbers are calculated by the following formula:
        fibonacci(0) = 0
        fibonacci(1) = 1
        fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)
    HINT:
    The following "pseudocode" describes how to calculate the nth fibonacci number:
    Let f0 = 0
    Let f1 = 1
    In a for loop from 0 to n,
        Let fn = f0 + f1
        Let f0 = f1
        Let f1 = fn
    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
    >>> fibonacci(2)
    1
    >>> fibonacci(3)
    2
    >>> fibonacci(4)
    3
    >>> fibonacci(5)
    5
    >>> fibonacci(6)
    8
    >>> fibonacci(7)
    13
    >>> fibonacci(1000)
    43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875
    '''
