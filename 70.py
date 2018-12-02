class Solution:
    def combineCal(self, total, uniq):
        combine = 1
        exclude = 1
        for i in range(uniq):
            combine = combine*(total-i)
            exclude = exclude*(uniq-i)
        return int(combine/exclude)

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        n2 = n//2
        n1 = n%2
        sumstep=1
        while n2!=0:
            uniq = n2
            total = n1+n2
            step = self.combineCal(total,uniq)
            #print(total, uniq, step)
            sumstep = sumstep+step
            n2-=1
            n1+=2
        return sumstep

print(Solution().climbStairs(6))
print(Solution().combineCal(3,3))