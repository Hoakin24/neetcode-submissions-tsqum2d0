class Solution:
    def isPalindrome(self, s: str) -> bool:
        formatted_string = "".join(c for c in s if c.isalnum()).lower()
        start = 0
        end = len(formatted_string) - 1

        print(formatted_string)
        print(start)
        print(end)

        while start <= end:
            if formatted_string[start] != formatted_string[end]: return False
            start += 1
            end -= 1
        
        return True