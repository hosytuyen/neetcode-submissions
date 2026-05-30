class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        l = 0
        freq = {}
        max_freq = 0
        for r in range(len(s)):
            sub_string = s[l:r+1]
            freq[s[r]] = freq.get(s[r], 0) + 1
            max_freq = max(max_freq, freq[s[r]])
            if (r+1-l) - max_freq > k:
                freq[s[l]] -= 1
                l += 1
            max_len = max(max_len, (r+1-l))
        return max_len
                

                


        