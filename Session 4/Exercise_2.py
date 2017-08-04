
prices = {}

prices["banana"] = 4
prices["apple"] = 2
prices["orange"] = 1.5
prices["pear"] = 3

print(prices)
print("*************************")

purchased_items = {
        "banana" : 5,
        "orange" : 3
    }

purchased_items["banana"] : 5
purchased_items["orange"] : 3

print(purchased_items)
print("*************************")

total = 0

for k in purchased_items.keys():
    print(k,", quantity:", purchased_items[k],", unit price: ", prices[k])

    sub_total = purchased_items[k]*prices[k]
    print("Sub_total: ", sub_total)
    print()
    total += sub_total

print("Total: ", total)


