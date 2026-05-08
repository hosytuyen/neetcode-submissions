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
        s = ''.join(c.lower() for c in s if self.valid_character(c))
        left_index = 0
        right_index = len(s) - 1

        print(s)

        while left_index < right_index:
            if s[left_index] == s[right_index]:
                left_index += 1
                right_index -= 1
                continue
            else:
                return False
        return True