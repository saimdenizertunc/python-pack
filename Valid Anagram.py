# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

def isAnagram(self, s: str, t: str) -> bool:
    if len(t) != len(s):
        return False
    return (sorted(list(s)) == sorted(list(t)))
