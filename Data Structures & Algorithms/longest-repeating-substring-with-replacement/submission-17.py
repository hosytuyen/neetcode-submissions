class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        l = 0
        while l < len(s):
            freq = {}
            max_freq = 0
            r = l
            while r < len(s):
                freq[s[r]] = freq.get(s[r], 0) + 1
                max_freq = max(max_freq, freq[s[r]])
                if r+1-l - max_freq <= k:
                    max_len = max(max_len, r+1-l)
                else:
                    break
                r += 1
            l += 1 
        return max_len
                

                


        