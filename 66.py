class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits[-1] += 1
        digits = digits[::-1]
        l = len(digits)
        k = 0
        for i in range(l):
            if digits[i] + k >= 10:
                digits[i] = (digits[i] + k) % 10
                k = 1
            else:
                digits[i] = digits[i] + k
                k = 0
            if k == 1 and i == l - 1:
                digits.append(k)

        return digits[::-1]
