from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        counts = {}
        for letter_s in s:
            if letter_s not in counts:
                counts[letter_s] = 1
            else: 
                counts[letter_s] += 1

        print(counts)
        for letter_t in t:
            if letter_t in counts:
                counts[letter_t] -= 1
            else: 
                counts[letter_t] = -1
        
        print(counts)
        for value in list(counts.values()):
            if value != 0: return False
        
        return True

        # count_s = {}
        # count_t = {}

        # longer_word = s if len(s) > len(t) else t
        # for i in range(len(longer_word)):
        #     if i >= len(s) or i >= len(t): return False

        #     if s[i] in count_s:
        #         count_s[s[i]] += 1
        #     else:
        #         count_s[s[i]] = 1

        #     if t[i] in count_t:
        #         count_t[t[i]] += 1
        #     else:
        #         count_t[t[i]] = 1

        # return count_s == count_t