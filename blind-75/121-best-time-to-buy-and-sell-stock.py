
# let's break down the problem first
# ou're given an array prices where prices[i] is the stock price on day i.

#  Goal:: find the max profit we can make by buying on one day and selling on a future day

# Rules: can't sell before buying 
# if can't make any profit return 0

# Building the intuition ----->
# we want to find::
    # the "lowest price so far" --> as best buying day
    # the "biggest profit" ---> if sold on the current day to max the profit
    
    


def maxProfit(prices):
    min_price = float('inf')       # here min_profit starts as infinity so that any real price will be lower and replace it later
    max_profit = 0
    
    for price in prices:
        if min_price > price:
            min_price = price
        else:
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit
                
    return max_profit


prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))  # Expected Output: 5


prices = [5, 5, 5, 5, 5]
print(maxProfit(prices))  # Output: 0


prices = [9, 8, 7, 6, 5, 4]
print(maxProfit(prices))  # Output: 0


prices = [1, 2, 3, 4, 5, 6, 7]
print(maxProfit(prices))  # Output: 6

prices = [100]
print(maxProfit(prices))  # Output: 0


# very large input (stress test)

prices = [100000] + list(range(99999, 0, -1))
print(maxProfit(prices))  # Output: 0
