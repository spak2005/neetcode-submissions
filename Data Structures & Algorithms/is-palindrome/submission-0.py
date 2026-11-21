class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha_num = ""
        val = s.replace(" ", "")

        print(val)

        for char in val:
            if char.isalnum():
                alpha_num += char
        print(alpha_num)
        
        return alpha_num.lower() == alpha_num[::-1].lower()
