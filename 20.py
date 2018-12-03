class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = ["(", "{", "[" ]
        right = [")", "}", "]" ] 

        lenstr = len(s)

        if lenstr%2!=0:
        	return False
        
        seq = []
        
        for i in range(lenstr):
        	if s[i] in left:
        		temp_left = left.index(s[i])
        		seq.append(temp_left)
        	if s[i] in right:
        		if i ==0:
        			return False
        		temp_right = right.index(s[i])
        		if temp_right==seq[-1]:
        			seq.pop()
        		else:
        			return False

        return seq==[]