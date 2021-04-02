# Task_1
# Write a function that takes an integer as input, and returns the number of bits that are equal to one in
# the binary representation of that number. You can guarantee that input is non-negative.
#
# Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case

def count_bits(n: int):
    result = []
    while n:
        result.append(n % 2)
        n //= 2

    result.reverse()
    result = [str(el) for el in result]
    return int(''.join(result))


# Task_2
# Build Tower
# Build Tower by the following given argument:
# number of floors (integer and always greater than 0).
# Tower block is represented as *

def tower_builder(n_floors):
    return [' ' * (n_floors - 1 - n) + '*' * (2 * n + 1) + ' ' * (n_floors - 1 - n) for n in range(n_floors)]


# Task_3
# Complete the solution so that it splits the string into pairs of two characters.
# If the string contains an odd number of characters then it should replace
# the missing second character of the final pair with an underscore ('_').
#
# Examples:
# solution('abc') # should return ['ab', 'c_']
# solution('abcdef') # should return ['ab', 'cd', 'ef']

def solution(string):
    if len(string) % 2 == 0:
        return [string[i] + string[i+1] for i in range(0, len(string), 2)]
    else:
        string = string + '_'
        return [string[i] + string[i + 1] for i in range(0, len(string), 2)]


# Task_4
# Welcome.
# In this kata you are required to, given a string, replace every letter with its position in the alphabet.
# If anything in the text isn't a letter, ignore it and don't return it.
# "a" = 1, "b" = 2, etc.
#
# Example
# alphabet_position("The sunset sets at twelve o' clock.")
# Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" (as a string)

def alphabet_position(text):
    string = 'abcdefghijklmnopqrstuvwxyz'
    text = list(filter(lambda x: x.isalpha(), text))
    return ' '.join([str(string.index(el.lower()) + 1) for el in text])


# Task_5
# The Western Suburbs Croquet Club has two categories of membership, Senior and Open.
# They would like your help with an application form that will tell prospective members
# which category they will be placed.
# To be a senior, a member must be at least 55 years old and have a handicap greater than 7.
# In this croquet club, handicaps range from -2 to +26; the better the player the lower the handicap.
#
# Input
# Input will consist of a list of lists containing two items each. Each list contains information
# for a single potential member.
# Information consists of an integer for the person's age and an integer for the person's handicap.
# Note for F#: The input will be of (int list list) which is a List<List>
#
# Example
# Input
# [[18, 20],[45, 2],[61, 12],[37, 6],[21, 21],[78, 9]]
# Output
# Output will consist of a list of string values (in Haskell: Open or Senior)
# stating whether the respective member is to be placed in the senior or open category.
# Example Output
# ["Open", "Open", "Senior", "Open", "Open", "Senior"]
def open_or_senior(data):
    return ['Senior' if chunk[0] >= 55 and chunk[1] > 7 else 'Open' for chunk in data]


# Task_6
def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    return (sq**0.5 + 1)**2 if int(sq**0.5)**2 == sq else -1


# Task_7

# Given a string of words, you need to find the highest scoring word.
# Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
# You need to return the highest scoring word as a string.
# If two words score the same, return the word that appears earliest in the original string.
# All letters will be lowercase and all inputs will be valid.

def high(string):

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = []
    string = string.split()

    for word in string:
        result.append(sum([alphabet.index(el.lower()) + 1 for el in word]))

    return string[result.index(max(result))]

# def high(x):
#     return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))


# Task_8
# Trolls are attacking your comment section!
# A common way to deal with this situation is to remove all of the vowels from the trolls' comments,
# neutralizing the threat.
# Your task is to write a function that takes a string and return a new string with all vowels removed.
# For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
# Note: for this kata y isn't considered a vowel.

def disemvowel(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return ''.join(list(filter(lambda x: x.lower() not in vowels, string)))


# Task_9
# Complete the method/function so that it converts dash/underscore delimited words into camel casing.
# The first word within the output should be capitalized only if the original word was capitalized
# (known as Upper Camel Case, also often referred to as Pascal case).
#
# Examples
# "the-stealth-warrior" gets converted to "theStealthWarrior"
# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"

def to_camel_case(text):
    text = text.replace('_' and '-', ' ').split()
    return text[0] + ''.join([text[i].capitalize() for i in range(1, len(text))])


# Task_10
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
#
# Note: If the number is a multiple of both 3 and 5, only count it once. Also, if a number is negative,
# return 0(for languages that do have them)

def solution_1(number):
    return 0 if number < 0 else sum(list(filter(lambda x: x % 3 == 0 or x % 5 == 0, range(number))))


# Task_11
# Write a function that takes in a string of one or more words, and returns the same string,
# but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist
# of only letters and spaces. Spaces will be included only when more than one word is present.
#
# Examples:
# spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw"
# spinWords( "This is a test") => returns "This is a test"
# spinWords( "This is another test" )=> returns "This is rehtona test"

def spin_words(sentence):
    result = list(map(lambda word: word if len(word) < 5 else word[::-1], sentence.split()))
    return ' '.join(result)


# Task_12
# You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or
# other items. We want to create the text that should be displayed next to such an item.
# Implement a function likes :: [String] -> String, which must take in input array, containing the names of
# people who like an item. It must return the display text as shown in the examples:
#
# likes([]) # must be "no one likes this"
# likes(["Peter"]) # must be "Peter likes this"
# likes(["Jacob", "Alex"]) # must be "Jacob and Alex like this"
# likes(["Max", "John", "Mark"]) # must be "Max, John and Mark like this"
# likes(["Alex", "Jacob", "Mark", "Max"]) # must be "Alex, Jacob and 2 others like this"
# For 4 or more names, the number in and 2 others simply increases.

def likes(names):
    if len(names) == 0:
        return 'no one likes this'
    elif len(names) == 1:
        return f'{names[0]} likes this'
    elif len(names) == 2:
        return f'{names[0]} and {names[1]} like this'
    elif len(names) == 3:
        return f'{names[0]}, {names[1]} and {names[2]} like this'
    elif len(names) > 4:
        return f'{names[0]}, {names[1]} and {len(names) - 2} others like this'


# Task_13
# Digital root is the recursive sum of all the digits in a number.
# Given n, take the sum of the digits of n. If that value has more than one digit,
# continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.
#
# Examples
#     16  -->  1 + 6 = 7
#    942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
# 132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
# 493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2

from functools import reduce


def digital_root(number):
    if len(str(number)) == 1:
        return number
    number = reduce(lambda res, x: res + x, map(int, str(number)))
    return digital_root(number)


# Task_14
# You live in the city of Cartesia where all roads are laid out in a perfect grid.
# You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk.
# The city provides its citizens with a Walk Generating App on their phones -- everytime you press the button it sends
# you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']). You always walk only
# a single block for each letter (direction) and you know it takes you one minute to traverse one city block, so create
# a function that will return true if the walk the app gives you will take you exactly ten minutes
# (you don't want to be early or late!) and will, of course, return you to your starting point. Return false otherwise.
#
# Note: you will always receive a valid array containing a random assortment of direction
# letters ('n', 's', 'e', or 'w' only). It will never give you
# an empty array (that's not a walk, that's standing still!).

def is_valid_walk(walk):
    if len(walk) != 10:
        return False
    else:
        return True if walk.count('s') == walk.count('n') and walk.count('w') == walk.count('e') else False


# Task_15
# Implement the function unique_in_order which takes as argument a sequence and returns a list of items without
# any elements with the same value next to each other and preserving the original order of elements.
#
# For example:
# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1,2,2,3,3])       == [1,2,3]

def unique_in_order(iterable):
    indices = list(filter(lambda i: iterable[i] != iterable[i-1], range(1, len(iterable))))
    return [iterable[0]] + [iterable[i] for i in indices] if len(iterable) != 0 else []

# from itertools import groupby
#
# def unique_in_order(iterable):
#     return [k for (k, _) in groupby(iterable)]


# Task_16
# Определить, является ли число простым?
def is_prime(num):
    if num == 2:
        return True
    elif num < 2:
        return False
    elif num != 2 and num % 2 == 0:
        return False
    else:
        return all(num % i for i in range(3, int(num**0.5)+1))


def main():
    # Task_1
    # print(count_bits(1234))
    # Task_2
    # print(tower_builder(3))
    # Task_3
    # print(solution('abcd'))
    # print(solution('abcde'))
    # Task_4
    # print(alphabet_position("The sunset sets at twelve o' clock."))
    # Task_5
    # print(open_or_senior([[18, 20],[45, 2],[61, 12],[37, 6],[21, 21],[78, 9]]))
    # Task_7
    # print(high('man i need a taxi up to ubud'))
    # Task_8
    # print(disemvowel("This website is for losers LOL!"))
    # Task_9
    print(to_camel_case("the-stealth-warrior"))
    # Task_10
    # print(solution_1(12))
    # Task_11
    # print(spin_words("Hey fellow warriors"))
    # Task_12
    # print(digital_root(16))
    # Task_14
    # print(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']))
    # print(is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e']))
    # Task_15
    # print(unique_in_order('AAAABBBCCDAABBB'))
    # Task_16
    print(is_prime(2))


if __name__ == '__main__':
    main()
