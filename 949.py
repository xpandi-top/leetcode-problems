class Solution:
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        flag = 0
        A.sort()
        B = [x for x in A]
        if 2 in A:
            hour = 2
            A.remove(2)
            ml = [x for x in A if x in range(0,4)]
            if ml!=[]:
                minute = ml[-1]
                A.remove(minute)
                sl = [x for x in A if x in range(0,6)]
                if sl!=[]:
                    flag=1
                    sec = sl[-1]
                    A.remove(sec)
                    end=A[-1]
        if flag==0:
            A = [x for x in B]
        if flag==0 and 1 in A:
            hour = 1
            A.remove(hour)
            sl = [x for x in A if x in range(0,6)]
            if sl!=[]:
                flag = 1
                if len(sl)==1:
                    sec = sl[-1]
                    A.remove(sec)
                    minute = A[-1]
                    end = A[0]
                elif len(sl)==3:
                    minute = sl[2]
                    sec = sl[1]
                    end = sl[0]
                else:
                    minute = max(A)
                    A.remove(minute)
                    sl = [x for x in A if x in range(0,6)]
                    sec = sl[-1]
                    A.remove(sec)
                    end=A[-1]
        if flag==0:
            A = [x for x in B]
        if flag==0 and 0 in A:
            hour = 0
            A.remove(hour)
            sl = [x for x in A if x in range(0,6)]
            if sl!=[]:
                flag = 1
                if len(sl)==1:
                    sec = sl[-1]
                    A.remove(sec)
                    minute = A[-1]
                    end = A[0]
                elif len(sl)==3:
                    minute = sl[2]
                    sec = sl[1]
                    end = sl[0]
                else:
                    minute = max(A)
                    A.remove(minute)
                    sl = [x for x in A if x in range(0,6)]
                    sec = sl[-1]
                    A.remove(sec)
                    end=A[-1]
        if flag == 0:
            rstr =""
        else:
            rstr = str(hour)+str(minute)+":"+str(sec)+str(end)
        return rstr
