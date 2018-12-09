class Solution(object):

    def canReorderDoubled(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        uniq = list(set(A))
        uniq.sort()
        countList = [A.count(i) for i in uniq]
        dictionary = dict(zip(uniq, countList))

        while len(uniq):
            comp1 = uniq[0]
            uniq.remove(comp1)
            if comp1 < 0:
                comp2 = int(comp1 / 2)
            elif comp1 == 0:
                if dictionary[comp1] % 2 != 0:
                    return False
                comp2 = 0
            else:
                comp2 = int(comp1 * 2)

            if comp2 != 0 and comp2 in uniq:
                if dictionary[comp1] > dictionary[comp2]:
                    return False
                elif dictionary[comp2] == dictionary[comp1]:
                    uniq.remove(comp2)
                else:
                    dictionary[comp2] = dictionary[comp2] - dictionary[comp1]
                    if len(uniq) == 1:
                        return False
            elif comp2 != 0 and comp2 not in uniq:
                return False

        return True


A = [-4, -6, -1, -2, -1, -1, -3, -8]
print(Solution().canReorderDoubled(A))
