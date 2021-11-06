# 01.py

# In this task you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

def filter_list(lst):
    return list(filter(lambda el: type(el) in (int, float), lst))

# 02.py

# Write a function named 'first_non_repeating_letter' that takes a string input, and returns the first character that is not repeated anywhere in the string.
# For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in the string, and occurs first in the string.
# As an added challenge, upper- and lowercase letters are considered the same character, but the function should return the correct case for the initial letter. 
# For example, the input 'sTreSS' should return 'T'.
# If a string contains all repeating characters, it should return an empty string ("") or None -- see sample tests.

def first_non_repeating_letter(value):
    if len(value) == 0:
        return None
    
    for ch in value:
        if value.lower().count(ch.lower()) == 1:
            return ch
    return None

# 03.py
# Task ?3

# Digital root is the recursive sum of all the digits in a number.
# Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.
# Examples:
# digital_root(16)
# => 1 + 6
# => 7

# digital_root(942)
# => 9 + 4 + 2
# => 15 ...
# => 1 + 5
# => 6

# digital_root(132189)
# => 1 + 3 + 2 + 1 + 8 + 9
# => 24 ...
# => 2 + 4
# => 6

# digital_root(493193)
# => 4 + 9 + 3 + 1 + 9 + 3
# => 29 ...
# => 2 + 9
# => 11 ...
# => 1 + 1
# => 2

def digital_root(value):
    result = sum(map(int, str(value)))
    if result > 9:
        result = digital_root(result)
    return result 

# 04.py
# Task ?4

# There is an array of numbers - arr [1, 3, 6, 2, 2, 0, 4, 5] 
# there is a number target = 5.
# Count the number of pairs in the array, the sum of which will give target

from itertools import combinations

def number_of_pairs(lst, target):
    return  sum(map(lambda item_pair: 1 if sum(item_pair)==target else 0, combinations(lst, 2)))

# 05.py
# Task ?5

# Den has invited some friends. His list is:

# s = "Fired:Corwill;Wilfred:Corwill;Barney:TornBull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill";

# Could you make a program that
# ? makes this string uppercase
# ? gives it sorted in alphabetical order by last name.
# When the last names are the same, sort them by first name. Last name and first name of a guest come in the result between parentheses separated by a comma.
# So the result of function meeting(s) will be:
# Examples:

# "(CORWILL, ALFRED)(CORWILL, FRED)(CORWILL, RAPHAEL)(CORWILL, WILFRED)(TORNBULL, BARNEY)(TORNBULL, BETTY)(TORNBULL, BJON)"


# It can happen that in two distinct families with the same family name two people have the same first name too.


def sort_friends(value):
    lst_friends = [tuple(person.split(":")) for person in value.split(";")]
    lst_friends.sort(key=lambda person: (person[1], person[0]))
    print("".join(map(lambda person: f"({person[1].upper()}, {person[0].upper()})", lst_friends)))

# 06.py
# Extra tasks
# Task 1
# Create a function that takes a positive integer and returns the next bigger number that can be formed by rearranging its digits.

# Examples:

# nextBigger(num: 12)    // returns 21
# nextBigger(num : 513)  //  returns 531 
# nextBigger(num : 2017  //  returns 2071




# If the digits can't be rearranged to form a bigger number, return -1

#  9  =>  -1
# 111 =>  -1
# 531 =>  -1

from itertools import permutations

def nextBigger(value):
    s_val = str(value)
    set_comb = set(list(permutations(s_val, len(s_val))))
    int_comb = sorted(list(map(lambda el: int("".join(el)), set_comb)))
    try:
        return int_comb[int_comb.index(value)+1]
    except:
        return -1

# # 07.py
# Extra tasks
# Task 2

# Take the following IPv4 address: 128.32.10.1
# This address has 4 octets where each octet is a single byte (or 8 bits).
# ? 1st octet 128 has the binary representation: 10000000
# ? 2nd octet 32 has the binary representation: 00100000
# ? 3rd octet 10 has the binary representation: 00001010
# ? 4th octet 1 has the binary representation: 00000001
# So 128.32.10.1 == 10000000.00100000.00001010.00000001
# Because the above IP address has 32 bits, we can represent it as the unsigned 32 bit number: 2149583361
# Complete the function that takes an unsigned 32 bit number and returns a string representation of its IPv4 address.
# Examples:

# 2149583361  =>  "128.32.10.1"
# 32 =>   "0.0.0.32"
# 0  =>   "0.0.0.0"

# 2_5199595594468823382.txt
# ?????? 2_5199595594468823382.txt.

def ip32_to_txt(value):
    s = ("00000000" + f"{value:02x}")[-8:]
    lst = [str(int(s[i*2: i*2+2], 16)) for i in range(len(s) // 2)]
    return ".".join(lst)