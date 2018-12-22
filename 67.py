class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a) > len(b):
            a = a[::-1]
            b = b[::-1]
        else:
            trans = a
            a = b[::-1]
            b = trans[::-1]

        k = 0
        news = []
        for i in range(len(a)):
            if i < len(b):
                temp = int(a[i]) + int(b[i]) + k
            else:
                temp = int(a[i]) + k

            if temp >= 2:
                temp = temp - 2
                k = 1
            else:
                k = 0

            news.append(temp)
            if k == 1 and i == len(a) - 1:
                news.append(k)
        news = news[::-1]

        return "".join([str(i) for i in news])
