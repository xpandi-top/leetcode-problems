class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs==[]:
            return ""
        words = strs
        minlen = min([len(word) for word in words])
        if minlen==0:
        	return ""
        flag = 1
        for i in range(minlen):
        	print(i)
        	for word in words[1:]:
        		if word[i]!=words[0][i]:
        			flag=0
        	prelen = i
        	if flag==0 :
        		break
        if flag==1:
        	prelen = i+1

        return words[0][:prelen]