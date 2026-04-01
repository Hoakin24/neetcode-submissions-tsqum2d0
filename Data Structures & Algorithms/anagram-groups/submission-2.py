from string import ascii_lowercase

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_map = {}

        for word in strs:
            word_arr = [0] * 26
            for letter in word:
                index = ord(letter) - ord('a')
                word_arr[index] += 1
            
                 
            
            # curr_s = "".join(sorted(s))
            # print(s)
            # print(curr_s)

            tupled_word_arr = tuple(word_arr)
            if tuple(tupled_word_arr) not in str_map:
                str_map[tupled_word_arr] = [word]
            else: 
                str_map[tupled_word_arr].append(word)
        return list(str_map.values())