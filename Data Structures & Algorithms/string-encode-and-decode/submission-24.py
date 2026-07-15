class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = []
        for s in strs:
            encoded_string.append(f"{len(s)}/{s}")
        return "".join(encoded_string)
        
    def decode(self, s: str) -> List[str]:
        decoded_strs = [] 
        curr_index = 0
        # print(f"Encoded string: {s}")
        while curr_index < len(s):
            length = ''
            while s[curr_index] != '/':
                length += s[curr_index]
                curr_index += 1
            decoded_word = s[curr_index+1:curr_index+1+int(length)]
            decoded_strs.append(decoded_word)
            curr_index = curr_index+1+int(length)
        
        return decoded_strs

