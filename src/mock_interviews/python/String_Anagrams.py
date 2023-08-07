from collections import Counter

"""
Problem: String Anagrams

Statement:

- You are given the following input:

1. words: list of strings
2. target (string): a word that gets compared with words in the words list

Your goal is to find how many words in the list of words are anagrams of the target string.

Hint:

- An anagram is defined as the following:

1. The word uses the exact same characters as the other word.
2. The word can be rearranged, but still uses same number of characters as the other word.
3. The number of times the characters are used has to be the same.

Anagram Example: 'abc' -> 'cab' -> 'bca'
Anagram Example: 'parse' -> 'sprae' -> 'arspe'

"""

def is_anagram_v3(word_one, word_two):
    return Counter(word_one) == Counter(word_two)

# Feel free to define helper functions here
def is_anagram(word_one, word_two):
    counter_dict_one = dict(Counter(word_one))
    counter_dict_two = dict(Counter(word_two))

    tally = 0

    for key in counter_dict_one.keys():
        one_value = counter_dict_one[key]
        two_value = counter_dict_two[key]

        if one_value == two_value:
            tally += 1
    
    return tally == len(counter_dict_one)
        
def number_anagrams_v3(words: list, target:str) -> int:
    # Get words that have the same length
    words_same_length = filter(lambda word: len(word) == len(target), words)
    final_anagrams = filter(lambda x: is_anagram_v3(x, target), words_same_length)

    tally = 0

    for anagram in final_anagrams:
        tally += 1
    
    return tally

def number_anagrams_v2(words:list, target:str) -> int:
    # Set up a counter 
    counter = 0
    
    # Iterate word in words
    for word in words:
        if is_anagram(word, target) == True:
            counter += 1
    
    return counter



word = ['tents', 'cabb', 'cat', 'phone', 'abbc', 'acb']
target = 'bbac'

# Starter Code
def number_anagrams_v1(words: list, target: str) -> int:
    # TODO
    y=0
    for i in words:
        x=0
        for letter in i:
            if letter in target:
                x=x+1
        if x == len(i) and len(i)==len(target):
            y=y+1
    return y

def is_anagram(word_one, word_two):
    return Counter(word_one) == Counter(word_two)

def number_anagrams_v4(words: list, target: str) -> int:
    # Counter
    counter = 0

    for word in words:
        if len(word) != len(target):
            continue
        else:
            if is_anagram(word, target) == True:
                counter += 1
    
    return counter

# # print(number_anagrams(word,target))
# print(dict(Counter(target)))

# print(number_anagrams_v3(word, target))

counter_result = number_anagrams_v4(word, target)

print(counter_result) 