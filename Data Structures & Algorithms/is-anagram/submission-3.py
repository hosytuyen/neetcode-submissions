class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s_sort = sorted(s)
        # t_sort = sorted(t)
        # if len(s_sort) != len(t_sort):
        #     return False
        # for i in range(len(s_sort)):
        #     if s_sort[i] != t_sort[i]:
        #         return False
        # return True

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
        