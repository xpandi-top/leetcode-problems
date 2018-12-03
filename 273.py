class Solution:
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        I2E={1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",
             7:"Seven", 8:"Eight", 9:"Nine", 10:"Ten", 
             11:"Eleven", 12:"Twelve", 13:"Thirteen",14:"Fourteen", 15:"Fifteen",
             16:"Sixteen", 17:"Seventeen", 18:"Eighteen",19:"Nineteen", 20:"Twenty",
             30:"Thirty", 40:"Forty", 50:"Fifty", 60:"Sixty", 70:"Seventy", 80:"Eighty",
             90:"Ninety", 100:"Hundred",1000:"Thousand", 1000000:"Million", 1000000000:"Billion"}
        words=""
        last=1
        if num == 0:
        	return "Zero"
        while num>0:
        	print(num)
        	if num >= 1000**3:
        		n2w = num//(1000**3)
        		num = num%(1000**3)
        		words = words + " " + I2E[n2w] + " " + I2E[1000**3]
        	elif num >= 1000**2:
        		n2w = num//(1000**2)
        		num = num%(1000**2)
        		inwords=self.numberToWords(n2w)
        		words = words + " "+ inwords + " " + I2E[1000**2]
        	elif num >= 1000:
        		n2w = num//1000
        		num = num%1000
        		inwords=self.numberToWords(n2w)
        		words = words +" " + inwords + " " + I2E[1000]
        	elif num>=100:
        		n2w = num//100
        		num = num%100
        		inwords=self.numberToWords(n2w)
        		words = words +" " + inwords + " "+ I2E[100]
        	elif num>=20:
        		n2w = num//10*10
        		num = num%10
        		tenword=I2E[n2w]
        		words = words + " " + tenword
        	elif num>0:
        		n2w=num
        		num = 0
        		words = words +" "+ I2E[n2w]

        return " ".join(words.split())