def find_choclate(n,wrap):
    if n//wrap <= 0:
        return 0
    
    return n//wrap + find_choclate(n//wrap,wrap)

inp = input().split(" ")
money = int(inp[0])
price = int(inp[1])
wrap = int(inp[2])

start_choc = money // price
trade_choc = find_choclate(start_choc,wrap)
print(start_choc,trade_choc)
print(start_choc + trade_choc)