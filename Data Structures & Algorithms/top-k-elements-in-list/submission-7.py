class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        count = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))

        print(count)

        output = []
        count_i = 0
        for key, value in count.items():
            output.append(key)
            count_i += 1
            if count_i == k:
                break
        
        return output
        