# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

first_word = input(str("First Word: "))
second_word = input(str("Second Word:   "))


def find_anagram(first_word, second_word):
    # [assignment] Add your code here
    if (sorted(first_word)) == sorted(second_word):
        print("True")
    else:
        print("False")


find_anagram(first_word, second_word)

