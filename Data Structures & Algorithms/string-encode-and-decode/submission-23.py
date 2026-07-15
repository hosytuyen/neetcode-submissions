class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ''
        for s in strs:
            encoded_string += (f"{len(s)}/{s}")
        return encoded_string
        
    def decode(self, s: str) -> List[str]:
        decoded_strs = [] 
        curr_index = 0
        # print(f"Encoded string: {s}")
        while curr_index < len(s):
            length = ''
            while s[curr_index] != '/':
                length += s[curr_index]
                curr_index += 1
            # print(f"Word Length: {int(length)}")
            # print(curr_index)
            decoded_word = s[curr_index+1:curr_index+1+int(length)]
            decoded_strs.append(decoded_word)
            curr_index = curr_index+1+int(length)
            # print(f"Output list: {decoded_strs}")
            # print("\n")
        
        return decoded_strs

