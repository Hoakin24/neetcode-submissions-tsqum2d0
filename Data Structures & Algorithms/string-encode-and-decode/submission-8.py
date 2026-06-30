class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            str_len = len(s)
            partial_encoded_string = f"{str_len}#{s}"
            encoded_string += partial_encoded_string

        print(encoded_string)
        return encoded_string


    def decode(self, s: str) -> List[str]:
        decoded_string = []
        i = 0
        while i < len(s):
            print('before')
            print(i)
            str_len = ""
            while s[i].isnumeric():
                str_len += s[i]
                i += 1
            i+=1
            starting = i
            ending = i + int(str_len)
            print(f"word: {s[starting:ending]}")
            decoded_string.append(s[starting:ending])
            i = ending

            print('after')
            print(i)

        return decoded_string
