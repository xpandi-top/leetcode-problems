class Solution:
    def intToRoman(self, num):
        s=""
        while num>0:
        	if num>=1000:
        		s=s+"M"
        		num = num - 1000
        	elif num>=900:
        		s=s+"CM"
        		num = num - 900
        	elif num>= 500:
        		s=s+"D"
        		num = num - 500
        	elif num>=400:
        		s=s+"CD"
        		num = num - 400
        	elif num>=100:
        		s=s+"C"
        		num = num - 100
        	elif num>=90:
        		s=s+"XC"
        		num = num -90
        	elif num >=50:
        		s=s+"L"
        		num = num -50
        	elif num>=40:
        		s=s+"XL"
        		num = num - 40
        	elif num>=10:
        		s=s+"X"
        		num = num - 10
        	elif num>=9:
        		s=s+"IX"
        		num = num - 9
        	elif num>=5:
        		s=s+"V"
        		num = num -5
        	elif num>=4:
        		s=s+"IV"
        		num = num -4
        	elif num>=1:
        		s=s+"I"
        		num = num -1
        return s

i=1994
print(Solution().intToRoman(i))