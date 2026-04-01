class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for s in strs: 
            encoded += f'{len(s)}#{s}'
        # print(encoded)
        return encoded


    def decode(self, s: str) -> List[str]:
        i = 0
        print(f"s: {s}")
        output = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
                
            s_len = int(s[i:j])
            i = j + 1
            output.append(s[i : i + s_len])
            i = i + s_len
            
        return output
            


