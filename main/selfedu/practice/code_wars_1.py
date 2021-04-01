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
    print(high('man i need a taxi up to ubud'))


if __name__ == '__main__':
    main()
