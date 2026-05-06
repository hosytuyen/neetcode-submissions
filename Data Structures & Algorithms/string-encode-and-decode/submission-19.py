class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_s = ""
        for string in strs:
            s_length = len(string)
            encoded_s += f"{s_length:03d}#" + string
        return encoded_s

    def decode(self, s: str) -> List[str]:
        out = []
        i = 0
        while i < len(s):
            length = int(s[i:i+3])
            string = s[i+4:i+4+length]
            out.append(string)
            i += 4 + length
        return out
