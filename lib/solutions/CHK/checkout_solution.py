

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    prices = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15
    }

    if not skus:
        return 0
    basket = list(skus)
    if not all(item in prices for item in basket):
        return -1
    
    item_counts = {}
    for item in basket:
        item_counts[item] = item_counts.get(item,0) + 1
    
    total = 0

    count_a = item_counts["A"]
    total +
    
    return total

