# 100 Days of Code with Python
Following [code challenges](https://codechalleng.es/100days/community/100_days_of_awesome_python)

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

## Day 6
Write a simple property
Write a simple `Promo` class. Its constructor receives a name `str` and expires `datetime`.
Add a property called expired which returns a `bool`.

## Day 7
1. Given the provided cars dictionary:

   Get all Jeeps
   Get the first car of every manufacturer.
   Get all vehicles containing the string Trail in their names (should work for other grep too)
   Sort the models (`values`) alphabetically
2. Write a function to determine if a word (or phrase) is [a palindrome](https://en.wikipedia.org/wiki/Palindrome).
   Then write a second function to receive a word (or phrase) list and determine which word is the longest palindrome.

## Day 8
Dictionary comprehensions are awesome.
A dictionary comprehension is like a list comprehension, but it constructs a `dict` instead of a `list`. They are convenient to quickly operate on each (`key`, `value`) pair of a `dict`. And often in one line of code, maybe two after checking [PEP8](https://pep8.org/) ;)

We think they are elegant, that's why we want you to know about them!

In this Bite you are given a `dict` and a `set`. Write a dictionary comprehension that filters out the items in the set and returns the resulting dict, so if your dict is `{1: 'bob', 2: 'julian', 3: 'tim'}` and your set is `{2, 3}`, the resulting dict would be `{1: 'bob'}`.

## Day 9
1. Don't let mutability fool you
   n this Bite you are presented with a function that copies the given items data structure.
   There is a problem though, the tests fail. Can you fix it?
   This can be done in a one liner. If you know which module to use it will be easy, if not you will learn something new today.
   Regardless we want you to think about Python's mutability.
2. Martin is preparing to pass an IQ test.
   The most frequent task in this test is to find out which one of the given characters differs from the others. He observed that one char usually differs from the others in being alphanumeric or not.

   Please help Martin! To check his answers, he needs a program to find the different one (the alphanumeric among non-alphanumerics or vice versa) among the given characters.

   Complete `get_index_different_char` to meet this goal. It receives a chars list and returns an `int index` (zero-based).

   Just to be clear, `alphanumeric == abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`

   Examples:
   ```
   ['A', 'f', '.', 'Q', 2]  # returns index 2 (dot is non-alphanumeric among alphanumerics)
   ['.', '{', ' ^', '%', 'a']  # returns index 4 ('a' is alphanumeric among non-alphanumerics)
   ```

## Day 10
Rewrite a for loop using recursion
Although you have to be careful using recursion it is one of those concepts you want to at least understand. It's also commonly used in coding interviews :)

In this beginner Bite we let you rewrite a simple countdown for loop using recursion. See `countdown_for` below, it produces the following output:

```
$ python countdown.py
10
9
8
7
6
5
4
3
2
1
time is up
```

## Day 11
1. Using ElementTree to parse XML
   In this Bite you will use `ElementTree` to parse some [Nolan movies](https://www.imdb.com/name/nm0634240/) we extracted from [OMDb](https://www.omdbapi.com/).

   Luckily most APIs switched to JSON, but sometimes XML is all there is, so at least learn to parse some! Complete the `get_tree`, `get_movies` and `get_movie_longest_runtime` functions below. See the docstrings and tests for more info.
2. Write a decorator called `make_html` that wraps text inside one or more html tags.

   As shown in the tests decorating `get_text` with `make_html` twice should wrap the text in the corresponding html tags, so:
   ```
   @make_html('p')
   @make_html('strong')
   def get_text(text='I code with PyBites'):
       return text
   ```
   - would return: `<p><strong>I code with PyBites</strong></p>`

## Day 12
Write a function called `gen_key` that creates a license key with this format: `KI80OMZ7-5OGYC1AC-735LDPT1-4L11XU1U`. The key consists of a combination of upper case letters and digits.

It takes two arguments: `parts` and `chars_per_part` which default to 4 and 8 respectively, so you can call the function like:

 - `gen_key()` to get a similar key as above, or
 - as `gen_key(parts=3, chars_per_part=4)` to get a shorter one, e.g.: 54N8-I70K-2JZ7.
Before you default to `random`, check if Python >= 3.6 has a better option available for this task 