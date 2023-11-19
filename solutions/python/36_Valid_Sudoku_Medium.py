class Solution(object):
    def IsValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool

        # S1 #
        1. Brute force is checking all the three rules one by one, traversing each row and column.
        2. We don't need to loop the board three times. We may check all three rules just once.

        # S2 #
        1. Overview: loop row and col, use three different array masks to save whether a number is visited in each row/col/subgroup
        2. Key point:
        2.1 row_visited: 2D bool array (m, 9)

        3. Complexity:
        3.1 time O(n2)
        3.2 space O(n)

        """
        m, n = len(board), len(board[0])
        num_group = (m // 3) * (n // 3)

        used1 = [[False for _ in range(10)] for _ in range(m)]  # row used
        used2 = [[False for _ in range(10)] for _ in range(n)]  # col used
        used3 = [[False for _ in range(10)] for _ in range(num_group)]  # group used

        for i in range(m):
            for j in range(n):
                if board[i][j] != '.':
                    num = int(board[i][j]) - 1
                    group_idx = i // 3 * 3 + j // 3
                    if used1[i][num] or used2[j][num] or used3[group_idx][num]:
                        return False
                    used1[i][num] = True
                    used2[j][num] = True
                    used3[group_idx][num] = True

        return True