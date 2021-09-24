'''
This file contains Wednesday's lecture notes.
================================================================================
Labs/quizzes are entered into sakai.
- Quiz average: 8.5  (up from 7.0 last week!)
  - 6 students with score <= 5
  - if that's you, re-evaluate your study techniques
  - all material is fair game for future quizzes
- Lab:
  - most students got 5/5
  - 7 students received a 0/5; common problems include
    - no submission
    - submitting the lab.py file instead of the doctests
    - not submitting the entire doctest output
      (often caused by an infinite loop in the num_digits function)
  - if you received a 0, please resubmit
    I will waive the late penalty for this lab
- Current overall average grade: 88.3
================================================================================
As a reminder, we've now seen 4 ways to run python:
    1. pythontutor.com
    2. $ python3 filename.py            # the "triangle button"
    3. $ python3 -m doctest filename.py # runs the doctests
    4. $ python3                        # runs "interactive python"
In order for python to be able to find your files,
you need to have the right folder open.
For some people, this means pressing the "pages button" in the left of vscode and then pressing "open folder".
For other people, this means running a command like
    $ cd foldername
in the terminal to "change directory" into the folder that contains your python files.
Today, we will see a 5th way to run python:
    5. $ python3 -i filename.py
The -i stands for interactive, and this is a special way to run interactive python that also loads the file and gives you access to all its internal functions and variables.
'''

import math

################################################################################
# lists
################################################################################

def largest(xs):
   #a column indicates a "piece" as a result; similar to the range function in the form of 1:3, 0:4 or etc 
    '''
    Return the largest element in the input list.
    If the list has no elements, return None.
    HINT:
    There are three ways to solve this problem:
    1. use a for loop + if statement
    2. sort the list and use list subscripting
    3. use a built-in function
    >>> largest([1,2,3])
    3
    >>> largest([99,-56,80,100,90])
    100
    >>> largest(list(range(0,100)))
    99
    >>> largest([10])
    10
    >>> largest([])
    '''
    if len(xs) == 0:
        return None
    biggest = 0
    for x in xs:
        if x > biggest:
            biggest = x
    return biggest


def largest_index(xs):
    '''
    Return the index of the largest element in the input list.
    If the list has no elements, return None.
    HINT:
    The sorting/built-in function approach will not work on this function.
    >>> largest_index([1,2,3])
    2
    >>> largest_index([99,-56,80,100,90])
    3
    >>> largest_index(list(range(0,100)))
    99
    >>> largest_index([10])
    0
    >>> largest_index([])
    '''
    #xs.sort() modifies the xs list anf puts it in their sorted order
    #dot commands modifies things
    '''if len(xs) == 0:
        return None
    xs.sort[-1]
    '''
    if len(xs) == 0:
        return None
    biggest = -math.inf
    biggest_index = None #keep track of the index in a new variable
    for i in range(len(xs)): #loops over the idexes instead of the vlaues
        x = xs[i]
        if x > biggest:
            biggest = xs[i]
            biggest_index = i
    return biggest_index

    


def filter_odd(xs):
    '''
    Return a list with all the odd elements removed.
    HINT:
    Use the accumulator pattern with a for loop.
    >>> filter_odd([1,3,5])
    []
    >>> filter_odd([2,4,6])
    [2, 4, 6]
    >>> filter_odd([4,5,6,7])
    [4, 6]
    >>> filter_odd([20,13,4,16,8,19,10])
    [20, 4, 16, 8, 10]
    '''
    accumulator=[]
    for x in xs:
        if x%2 == 0:
            accumulator.append(x)
    #add to the accunulator
    return accumulator

################################################################################
# dictionaries
################################################################################

# These dictionaries store the grades of famous people in their math, english, and economics classes.
# You shouldn't modify these dictionaries,
# they are used in the doctests for the functions below.
math_grades={
        'donald knuth':85, #left of : is the key
        'hypatia':75,      # right of : is the value
        'emmy noether':86, # each line is a (key, value) pair, and these pairs are separated by comas
        'leonhard euler':92, #each pair is "like" an item in a list
        'grigori perelman':95,
        'alexander grothendieck':95,
        'shelton cooper':72,
        'ada lovelace':96,
        }

english_grades={
        'emily dickenson':92,
        'edgar allan poe':88,
        'william shakespeare':84,
        'robert frost':83,
        'dorthy day':95,
        'douglas adams':42,
        'maya angelou':89,
        'emma goldman':85,
        }

economics_grades={
        'christine lagarde':85,
        'alan greenspan':92,
        'adam smith':88,
        'kristalina georgieva':79,
        'karl marx':90,
        'pierre-joseph proudhon':95,
        }

def lowest_grade(d):
    '''
    Return the largest value.
    >>> lowest_grade(math_grades)
    72
    >>> lowest_grade(english_grades)
    42
    >>> lowest_grade(economics_grades)
    79
    '''
    lowest = math.inf
    for key in d:
        grade = d[key]
        if grade < lowest:
            lowest = grade
    return lowest


def student_with_lowest_grade(d):
    '''
    Return the key that has the greatest value.
    >>> student_with_lowest_grade(math_grades)
    'shelton cooper'
    >>> student_with_lowest_grade(english_grades)
    'douglas adams'
    >>> student_with_lowest_grade(economics_grades)
    'kristalina georgieva'
    '''
    lowest = math.inf
    lowest_index = None
    for key in d:
         grade = d[key]
         if grade < lowest:
                lowest = grade
                lowest_index = key
    return lowest_index
