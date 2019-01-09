class Solution:
    def splitWord(self, word):
        uniqword = []
        uniqNum = []
        prev = ""
        i = -1
        for w in word:
            if w != prev:
                uniqword.append(w)
                uniqNum.append(1)
                i += 1
            else:
                uniqNum[i] += 1
            prev = w
        return uniqword, uniqNum

    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        num = 0
        addnum = 0
        uniqword, uniqnum = self.splitWord(S)
        for word in words:
            uniqw, uniqn = self.splitWord(word)
            if uniqw == uniqword:
                for i in range(len(uniqn)):
                    a = uniqnum[i]
                    b = uniqn[i]
                    if a > b:
                        if a > 2:
                            addnum = 1
                        else:
                            addnum = 0
                            break
                    elif a == b:
                        addnum = 1
                    else:
                        addnum = 0
                        break
            num = num + addnum
            addnum = 0
        return num
