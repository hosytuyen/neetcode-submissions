class Solution:
    def sort_string(self, string):
        string = sorted(string)
        string = ''.join(string)
        return string
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count_sorted_string = {}
        for i, string in enumerate(strs):
            sorted_str = self.sort_string(string)
            if sorted_str not in count_sorted_string:
                count_sorted_string[sorted_str] = [i]
            else:
                count_sorted_string[sorted_str].append(i)

        output = []
        for anagram_idx in count_sorted_string.values():
            anagram_strings = [strs[i] for i in anagram_idx]
            output.append(anagram_strings)

        return output

        