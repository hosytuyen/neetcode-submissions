class Solution:
    def count_freq(self, s):
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        return freq
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        for i in range(len(s)):
            freq = {}
            max_freq = 0
            for j in range(i, len(s)):
                sub_string = s[i:j+1]
                freq[s[j]] = freq.get(s[j], 0) + 1
                max_freq = max(max_freq, freq[s[j]])
                replace_needed = len(sub_string) - max_freq
                # print(sub_string, replace_needed)
                if replace_needed <= k:
                    max_len = max(max_len, len(sub_string))
        return max_len
                

                


        