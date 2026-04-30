class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hash_check = {}
        for char in s:
            hash_check[char] = hash_check.get(char, 0) + 1

        for char in t:
            if char not in hash_check:
                return False
            else:
                hash_check[char] -= 1
            if hash_check[char] == 0:
                hash_check.pop(char)
        if len(hash_check) != 0:
            return False
        
        return True
        