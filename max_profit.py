def max_profit(prices : list[int]) -> int:
    potential_profit = 0
    min_price = None
    max_profit = 0 
    for i in prices:
        # determine and keep record of the lowest price found 
        if min_price is None:
            min_price = i
        elif i < min_price:
            min_price = i
        # gives the profit for the current lowest price against current buy day
        potential_profit = i - min_price
        # if the potential profit is greater than the current max profit, it will be recorded for future comparisons
        # and ultimately to give the max profit found
        if potential_profit > max_profit:
            max_profit = potential_profit

    return max_profit

"""
Explanation of the logic: 
the min_price is used as a marker to find the lowest price point (buy day) to compare with the the future sell days, 
but we have the potential_profit making the comparative checks and storing the best profit in max_profit.
That way we only need to iterate through the list once (1 pass), and if there is a better profit margin, it'll be recorded in the max_profit else
we just keep iterating til the end of the list.

tldr:
min_price = cheapest price I have found
price - min_price = potential profit gained if I sell today (price)
max_profit = best profit made so far
"""

test_cases = [
    [7,1,5,3,6,4],
    [7,6,4,3,1]
]

for i in range(len(test_cases)):
    print(f"Test case {i}: {max_profit(test_cases[i])}")