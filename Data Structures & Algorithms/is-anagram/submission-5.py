import string 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = {char:0 for char in string.ascii_letters}
        hash_t = {char:0 for char in string.ascii_letters}
        for char in s:
            hash_s[char] += 1
        for char in t:
            hash_t[char] += 1
        for char, freq in hash_s.items():
            if hash_t[char] != freq:
                return False
        return True       