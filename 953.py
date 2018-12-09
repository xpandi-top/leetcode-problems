class Solution(object):
    def isOrder(self, compa, compb, order):
        minlen = min(len(compa), len(compb))
        for i in range(minlen):
            if order.index(compa[i]) < order.index(compb[i]):
                flag = True
                break
            elif order.index(compa[i]) > order.index(compb[i]):
                flag = False
                break
        if compa[:minlen] == compb[:minlen]:
            if len(compa) <= len(compb):
                flag = True
            else:
                flag = False
        return flag

    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        wordlen = len(words)
        if wordlen <= 1:
            return True

        for i in range(wordlen - 1):
            compa = words[i]
            compb = words[i + 1]
            if self.isOrder(compa, compb, order) == False:
                flag = False
                break
            else:
                flag = True
        return flag
