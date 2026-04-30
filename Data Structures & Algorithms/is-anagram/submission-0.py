class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = {}
        hash_t = {}

        for char in s:
            if char in hash_s:
                hash_s[char] += 1
            else:
                hash_s[char] = 1

        for char in t:
            if char in hash_t:
                hash_t[char] += 1
            else:
                hash_t[char] = 1

        if len(hash_s) != len(hash_t):
            return False

        for char, freq in hash_s.items():
            if char not in hash_t:
                return False
            if hash_t[char] != hash_s[char]:
                return False
        
        return True

        