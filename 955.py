class Solution:
    def minDeletionSize(self, A, tryCol=0):
        """
        :type A: List[str]
        :rtype: int
        """
        rows = len(A)
        isOrder = [A[i] <= A[i + 1] for i in range(rows - 1)]
        if all(isOrder) == True:
            removeColumns = 0
        else:
            isOrder_try = [A[i][0:tryCol + 1] <= A[i + 1][0:tryCol + 1] for i in range(rows - 1)]
            if all(isOrder_try) == True:
                tryCol = tryCol + 1
                removeColumns = self.minDeletionSize(A, tryCol)
            else:
                A = [A[i][0:tryCol] + A[i][tryCol + 1:] for i in range(rows)]
                removeColumns = 1 + self.minDeletionSize(A, tryCol)
        return removeColumns
