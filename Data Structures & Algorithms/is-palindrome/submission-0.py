class Solution:
    def isPalindrome(self, s: str) -> bool:
        only_alnum = "".join(char for char in s if char.isalnum())
        cleaned_text = only_alnum.lower() 
        set_up = list(cleaned_text)
        for i in range(len(set_up)): 
            if not set_up[i] == set_up[len(set_up)-1-i]: 
                return False 
        return True    