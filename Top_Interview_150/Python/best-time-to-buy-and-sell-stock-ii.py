class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit=0
        minvalue=prices[0]
        maxvalue=minvalue
        for i in range(1,len(prices)):
            if prices[i]>maxvalue:
                maxvalue=prices[i]
            else:
                maxprofit+=(maxvalue-minvalue)
                minvalue=prices[i]
                maxvalue=prices[i]
            if i == len(prices)-1:
                maxprofit+=(maxvalue-minvalue)
        return maxprofit
