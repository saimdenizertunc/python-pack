# Given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1.
# If a string is longer than the other, append the additional letters onto the end of the merged string.

def mergeAlternately(word1, word2):
    first_l = len(word1)
    second_l = len(word2)
    res = ''
    for i in range(min(first_l, second_l)):
        res += word1[i]
        res += word2[i]

    if (first_l == second_l):
        return res
    else:
        d = second_l - first_l
        if(d > 0):
            return res + word2[-d:]
        else:
            return res + word1[d:]
