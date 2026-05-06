class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_s = ""
        for string in strs:
            encoded_s += string + "."
        return encoded_s

    def decode(self, s: str) -> List[str]:
        return s.split(".")[:-1]
