# isalnum을 처음 알게 됨.
# isalnum : 문자열이 영문자 혹은 숫자인지 True or False로 판별해줌.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        data = list()
        
        for i in s:
            if i.isalnum():
                data.append(i.lower())
                
        if data == data[::-1]:
            return True
        
        return False