class Solution:
    def valid_character(self, c):
        if ord('a') <= ord(c) <= ord('z'):
            return True
        if ord('A') <= ord(c) <= ord('Z'):
            return True
        if ord('0') <= ord(c) <= ord('9'):
            return True
        return False

    def isPalindrome(self, s: str) -> bool:
        left_index = 0
        right_index = len(s) - 1
        s = s.lower()

        while left_index < right_index:
            while left_index < right_index and not self.valid_character(s[left_index]):
                left_index += 1
            while left_index < right_index and not self.valid_character(s[right_index]):
                right_index -= 1

            if s[left_index] != s[right_index]:
                return False
            left_index += 1
            right_index -= 1
        return True