class Solution:
    def maxProfit(self, prices) -> int:
        l = 0  # buy
        r = 1  # sell              here r =1 bcz minimum one day later i sell so here l=0 & more 1+ is selling day
        maxp=0
        while r < len(prices):      # runs whole array 
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxp = max(maxp,profit)  #compare b/w maxp & profit
            else:
                l = r   # its means we assing r value in l
            r += 1
        return maxp
