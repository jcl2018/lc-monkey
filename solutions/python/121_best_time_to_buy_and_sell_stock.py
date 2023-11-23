class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int


        # S1 #
        1. The brute force is to find out all pairs and check the maximum profit that you can get.
        2. Intuition: There's always a more optimized pick - say 1, 5, 9. we don't need to check 5 9 if we know 1 is smaller than 5
        # S2 #
        1. Overview: DP do one pass and update (1) current min (2) max profit.
        2. Key point
        3. Complexity:
        3.1 time O(n)
        3.2 space O(1)

        """
        min_value = float('inf')
        max_prof = 0
        for price in prices:
            if price > min_value:
                max_prof = max(max_prof, price - min_value)
            min_value = min(min_value, price)
        return max_prof
