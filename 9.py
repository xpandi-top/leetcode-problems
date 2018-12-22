class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        num = []
        if x < 0:
            return False

        while x > 0:
            temp = x % 10
            x = x // 10
            num.append(temp)

        return num == num[::-1]
