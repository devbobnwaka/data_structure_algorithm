import time
import test

print(__name__)

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result = ""
        word_len = 0
        if len(word1) > len(word2):
            word_len = len(word1)
        else:
            word_len = len(word2)

        print(word_len)
        for i in range(word_len):
            print(i)
            if i < len(word1):
                result += word1[i]
            if i < len(word2):
                result += word2[i]
        
        return result

# def sum_of_n_2(n):
#     start = time.time()
#     the_sum = 0
#     for i in range(1, n+1):
#         the_sum = the_sum + i
#     end = time.time()
#     return the_sum,end-start

# for i in range(5):
#     print("Sum is %d required %10.7f seconds" % sum_of_n_2(10000))

# def sum_of_n(n):
#     the_sum = 0
#     for i in range(1,n+1):
#         the_sum = the_sum + i
#     return the_sum
# print(sum_of_n(10))


# """
# Design a class to represent a playing card. Now design a class to represent a deck of
# cards. Using these two classes, implement a favorite card game.
# """

# class Card:
#     def __init__(self, suit, rank):
#         self.suit = suit
#         self.rank = rank

#     def get_suit(self):
#         return self.suit

#     def get_rank(self):
#         return self.rank

#     def __str__(self):
#         return f"{self.rank} of {self.suit}"

# class DeckOfCard:
#     def __init__(self):
#         self.cards = []

#         suits = ["Heart", "Spade", "Clubs", "Diamonds"]
#         ranks = ["ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king"]

#         for suit in suits:
#             for rank in ranks:
#                 self.cards.append(Card(suit, rank))
    
#     def __str__(self):
#         return ', '.join(map(str, self.cards))

# cards = DeckOfCard()
# print(cards)
        

# course = {"frontend": 200000, "backend": 150000, "copywriting": 50000}  
# # Unpack keys
# course1, course2, course3 = course
# print(course1)
# print(course2)
# print(course3)
# # Unpack values
# course1, course2, course3 = course.values()
# print(course1)
# print(course2)
# print(course3)
# # Unpack key value pair - a tuple
# course1, course2, course3 = course.items()
# print(course1)
# print(course2)
# print(course3)
# # Can also be used to combine too dictionary
# #e.g
# numbers = {"1":"one", "2": "two"}
# combine = {**course, **numbers}
# print(combine)

# """
# How can you swap the values of two variables without using a temporary variable.
# """

# fn = "Philip"
# ln = "Odulaja"

# fn, ln = ln, fn

# print(fn, ln)

# def gcd(m, n):
#     while m % n != 0:
#         old_m = m
#         old_n = n
#         m = old_n
#         n = old_m % old_n
#     return n
    
# class Fraction:

#     def __init__(self, top, bottom):
#         self.num = top
#         self.den = bottom

#     def get_num(self):
#         return self.num

#     def get_den(self):
#         return self.den

#     def __add__(self, other_fraction):
#         new_num = self.num*other_fraction.den + self.den*other_fraction.num
#         new_den = self.den * other_fraction.den
#         common = gcd(new_num, new_den)
#         return Fraction(new_num // common, new_den // common)

#     def __sub__(self, other_fraction):
#         new_num = self.num*other_fraction.den - self.den*other_fraction.num
#         new_den = self.den * other_fraction.den
#         common = gcd(new_num, new_den)
#         return Fraction(new_num // common, new_den // common)

#     def __mul__(self, other_fraction):
#         new_num = (self.num*other_fraction.num)
#         new_den = self.den * other_fraction.den
#         common = gcd(new_num, new_den)
#         return Fraction(new_num // common, new_den // common)

#     def __truediv__(self, other_fraction):
#         new_num = (self.num*other_fraction.den)
#         new_den = self.den * other_fraction.num
#         common = gcd(new_num, new_den)
#         return Fraction(new_num // common, new_den // common)

#     def __gt__(self, other_fraction):
#         first_num = self.num * other_fraction.den
#         second_num = other_fraction.num * self.den
#         return first_num > second_num

#     def __lt__(self, other_fraction):
#         first_num = self.num * other_fraction.den
#         second_num = other_fraction.num * self.den
#         return first_num < second_num

#     def __ge__(self, other_fraction):
#         first_num = self.num * other_fraction.den
#         second_num = other_fraction.num * self.den
#         return first_num >= second_num

#     def __le__(self, other_fraction):
#         first_num = self.num * other_fraction.den
#         second_num = other_fraction.num * self.den
#         return first_num <= second_num

#     def __eq__(self, other):
#         first_num = self.num * other.den
#         second_num = other.num * self.den
#         return first_num == second_num

#     def __ne__(self, other):
#         first_num = self.num * other.den
#         second_num = other.num * self.den
#         return first_num != second_num

#     def __str__ (self):
#         return str(self.num) + "/" + str(self.den)


# f1 = Fraction(2, 5)
# f2 = Fraction(1, 4)
# print(f1)


# import random

# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

# string=""
# while len(string) < len(letters):
#     random_num = random.randint(0,26)
#     string = string+letters[random_num]

# print(string)




# word_list = ['cat','dog','rabbit']
# letter_list = [ ]
# for word in word_list:
#     for letter in word:
#         if letter not in letter_list:
#             letter_list.append(letter)
# print(letter_list)

# ['c', 'a', 't', 'd', 'o', 'g', 'r', 'b', 'i']
# print(list(set(letter_list)))

# letter_list = []
# [letter_list.append(letter) for word in word_list for letter in word if letter not in letter_list ]
# print(letter_list)

    
"""
Implementing square root function using the well-known technique called
“Newton’s Method.” Newton’s Method for approximating square roots performs an iterative
computation that converges on the correct value. 

𝑛𝑒𝑤_𝑔𝑢𝑒𝑠𝑠 = 1 / 2 * (𝑜𝑙𝑑_𝑔𝑢𝑒𝑠𝑠 + (𝑛 / 𝑜𝑙𝑑_𝑔𝑢𝑒𝑠𝑠))

"""
# def square_root(num):
#     if num < 0:
#         raise ValueError("Cannot compute square root of a negative number")
#     if num == 0:
#         return 0
#     root = num / 2 #initial guess will be 1/2 of n
#     for k in range(20):
#         root = (1 / 2) * (root + (num / root))
#     return root

# print(square_root(9))


# animals = ["dog", "goat", "cow", "ram", "horse"]
# newlist = []

# for animal in animals:
#   if animal[1] == "o":
#     newlist.append(animal)

# print(newlist)



# ['dog', 'goat', 'cow', 'horse']



# newlist = [animal for animal in animals if animal[1] == "o"]

# print(newlist)


