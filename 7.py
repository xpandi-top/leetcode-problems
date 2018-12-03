
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if -2**31 < x <= 2**31-1:
            num = str(x)
        else:
            num=str(0)
        
        if num[0]=='-':
            renum='-'+ num[1:][::-1]
        else:
            renum=num[::-1]
        
        if -2**31 < int(renum) <= 2**31-1:
            renum=int(renum)
        else:
            renum=0
            
        return renum