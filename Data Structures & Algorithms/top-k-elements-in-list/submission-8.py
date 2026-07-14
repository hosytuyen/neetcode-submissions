class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        count = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))
        
        bucket = [[] for i in range(len(nums)+1)]
        for item, key in count.items():
            bucket[key].append(item)

        output = []
        for i in range(len(nums), 0, -1):
            k -= len(bucket[i])
            if k >= 0:
                for num in bucket[i]:
                    output.append(num) 
        
        return output
        