class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """Given two strings s and t, return true if t is an anagram of s, and false otherwise."""
        if sorted(s) == sorted(t):
            return True
        else:
            return False
