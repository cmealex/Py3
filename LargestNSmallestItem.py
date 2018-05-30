import heapq

grades = [1,2,3,4]
# print(heapq.nlargest(3, grades))

stocks = [
    {'t':'aa7', 'price':201},
    {'t':'aa6', 'price':202},
    {'t':'aa3', 'price':203},
    {'t':'aa4', 'price':204},
    {'t':'aa5', 'price':205}
]

# print(heapq.nsmallest(2, stocks, key=lambda stock: stock["t"]))