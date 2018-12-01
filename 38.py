class Solution:
    def numCount(self, number):
        l = len(number)
        newnumber = []
        for i in range(l):
            if i == 0:
                uniq = number[i]
                id = i
            if number[i] != uniq:
                newnumber.append(i - id)
                newnumber.append(uniq)
                uniq = number[i]
                id = i
            if i == l - 1:
                newnumber.append(l - id)
                newnumber.append(uniq)
        return newnumber

    def countAndSay(self, n):
        number = [1]
        if n == 1:
            return "1"
        else:
            for i in range(n - 1):
                newnumber = self.numCount(number)
                number = newnumber
        return ''.join([str(i) for i in newnumber])


number = [1, 1, 3, 2, 2]
print(Solution().numCount(number))
print(Solution().countAndSay(5))
