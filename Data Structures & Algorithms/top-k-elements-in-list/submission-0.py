class Solution:
    def count_freq(self, nums):
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        return freq
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = self.count_freq(nums)
        freq = sorted(freq.items(), key=lambda item: item[1], reverse=True)
        output = []
        for i in range(k):
            output.append(freq[i][0])
        return output

        