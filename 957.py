class Solution:
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        if N == 0:
            return cells
        rcells = [0] * 8
        for j in range(N % 14 + 14):
            for i in range(6):
                if cells[i] == cells[i + 2]:
                    rcells[i + 1] = 1
                else:
                    rcells[i + 1] = 0
            cells = [x for x in rcells]
        return cells
