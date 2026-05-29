class Solution:
    def count_freq(self, s):
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        return freq
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        l = r = 0
        while l < len(s):
            freq = {}
            max_freq = 0
            r = l
            while r < len(s):
                sub_string = s[l:r+1]
                freq[s[r]] = freq.get(s[r], 0) + 1
                max_freq = max(max_freq, freq[s[r]])
                replace_needed = len(sub_string) - max_freq
                if replace_needed <= k:
                    max_len = max(max_len, len(sub_string))
                else:
                    break
                r += 1
            l += 1 
        return max_len
                

                


        