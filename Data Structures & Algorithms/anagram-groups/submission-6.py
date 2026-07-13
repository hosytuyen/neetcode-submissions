class Solution:
    def count(self, string):
        count = [0]*26
        for char in string:
            count[ord(char)-ord('a')] += 1
        return tuple(count)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)
        for s in strs:
            key = self.count(s)
            output[key].append(s)
        return list(output.values())
        