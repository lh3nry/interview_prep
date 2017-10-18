# max_profit.py
import pprint as p

def maxProfit3(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if len(prices) < 2:
        return 0
    
    K = 2
    opt = [[0 for i in range(len(prices))] for i in range(K+1)]
    for i in range(1,K+1):
        prevtrans = opt[i-1][0] - prices[0]
        for j in range(1,len(prices)):
            opt[i][j] = max(opt[i][j-1], prices[j] + prevtrans)
            prevtrans = max(prevtrans, opt[i-1][j] - prices[j])
            print(prevtrans)
        print('',prices)
        p.pprint(opt)
            
    return opt[K][len(prices)-1]


def maxProfit4(k, prices):
    """
    :type k: int
    :type prices: List[int]
    :rtype: int
    """
    n = len(prices)
    if n < 2:
        return 0
    
    optmax = 0
    if k >= n//2:
        for i in range(n-1):
            optmax += max(prices[i+1]-prices[i],0)
        return optmax

    opt = [[0 for i in range(len(prices))] for i in range(k+1)]
    for i in range(1,k+1):
        optmax = opt[i-1][0] - prices[0]
        for j in range(1,len(prices)):
            opt[i][j] = max(opt[i][j-1], prices[j] + optmax)
            optmax = max(optmax, opt[i-1][j] - prices[j])
        # print(opt)
            
    return opt[k][len(prices)-1]
    
    # opt = prevopt = [0 for i in range(n)]
    # for i in range(1,k+1):
    #     optmax = prevopt[0] - prices[0]
    #     for j in range(1,len(prices)):
    #         opt[j] = max(opt[j-1], prices[j] + optmax)
    #         optmax = max(optmax, prevopt[j] - prices[j])
    #     print(prevopt,opt)
    #     prevopt = opt
    #     opt = [0 for i in range(len(prices))]
        
    # return prevopt[len(prices)-1]

def maxProfitCooldown(prices):
	n = len(prices)
	if n < 2: return 0
	buy = [float('-inf') for _ in range(n+1)]
	# buy = [0 for _ in range(n+1)]
	sell = [0 for _ in range(n+1)]

	for i in range(1,len(buy)):
		buy[i] = max(sell[i-2]-prices[i-1],buy[i-1])
		sell[i] = max(buy[i-1]+prices[i-1],sell[i-1])
		# print(buy)
		# print(sell)

	return sell[-1]


test = [7, 1, 5, 3, 6, 4, 3, 4, 1, 8]
test2 = [1, 2, 3, 0, 2]
# print(maxProfit3(test))
print(maxProfitCooldown(test2))

