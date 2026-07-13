class Solution:
    def count(self, string):
        count = {}
        for char in string:
            count[char] = count.get(char, 0) + 1
        count = dict(sorted(count.items()))
        count = ''.join(f"{key}{value}" for key, value in count.items())
        return count
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = {}
        for i in range(len(strs)):
            key = self.count(strs[i])
            if key not in output:
                output[key] = []
            output[key].append(strs[i])
        return [ana_group for _, ana_group in output.items()]
        