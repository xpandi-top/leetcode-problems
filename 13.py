class Solution:
    def romanToInt(self, s):
	    R2I = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
	    realI=0
	    rex=s[::-1]
	    flag2=1
	    flag=1
	    for index, roman in enumerate(rex):
		    flag2=1
		    if index+1<len(rex):
			    if roman == "M" or roman == "D" :
				    if rex[index+1]=="C":
					    flag2=-1
			    elif roman == "C" or roman =="L":
				    if rex[index+1]=="X":
					    flag2=-1
			    elif roman =="X" or roman == "V":
				    if rex[index+1]=="I":
					    flag2=-1
		    realI = R2I[roman]*flag+realI
		    flag = flag2
	    return realI
        