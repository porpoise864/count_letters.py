# Author: Sarah Oertly
# Date: 11/19/2019
# Descripton: Write a function named count_letters that takes as a parameter a string and returns a dictionary that
# tabulates how many of each letter is in that string. The string can contain characters other than letters, but only
# the letters should be counted. The string could even be the empty string. Lower-case and upper-case versions of a
# letter should be part of the same count. The keys of the dictionary should be the upper-case letters. If a letter does
# not appear in the string, then it would not get added to the dictionary. For example, if the string is
def count_letters(word, char):
    count = 0
    for c in word:
        if char == c:
            count += 1
    return count