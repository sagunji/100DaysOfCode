# 100 Days of Code with Python
Following (code challenges)[https://codechalleng.es/100days/community/100_days_of_awesome_python]

## Prerequisites
1. python
2. pytest

## Day 1
Sum n numbers
Write a function that can sum up numbers:
 - It should receive a list of n numbers.
 - If no argument is provided, return sum of numbers 1..100.
 - Look closely to the type of the function's default argument

## Day 2
Parse a list of names
First you will write a function to take out duplicates and title case them.

Then you will sort the list in alphabetical descending order by surname and lastly determine what the shortest first name is. For this exercise you can assume there is always one name and one surname.

With some handy Python builtins you can write this in a pretty concise way. Get it sorted :)

## Day 3
Write a function that rotates characters in a string, in both directions:

if n is positive move characters from beginning to end, e.g.: rotate('hello', 2) would return llohe
if n is negative move characters to the start of the string, e.g.: rotate('hello', -2) would return lohel

## Day 4
Iterate over the given names and countries lists, printing them prepending the number of the loop (starting at 1). Here is the output you need to deliver:
```
1. Julian     Australia
2. Bob        Spain
3. PyBites    Global
4. Dante      Argentina
5. Martin     USA
6. Rodolfo    Mexico
```
Notice that the 2nd column should have a fixed width of 11 chars, so between Julian and Australia there are 5 spaces, between Bob and Spain, there are 8. This column should also be aligned to the left.

Ideally you use only one for loop, but that is not a requirement.

## Day 5
Write a generator that returns special dates for PyBites:

- Every year mark counting from PYBITES_BORN date
- Every 100 days mark counting from PYBITES_BORN
