class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_length = 0
        for start in range(len(s)):
            end = start
            unique_charac = {}
            while end < len(s) and s[end] not in unique_charac:
                unique_charac[s[end]] = 1
                end += 1
            length = end - start
            print(length)
            longest_length = max(longest_length, length)
            start = end

        return longest_length

        