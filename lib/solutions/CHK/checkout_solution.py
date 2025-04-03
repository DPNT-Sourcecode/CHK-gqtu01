

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    prices = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15
    }

    special_offers = {
        'A': (3, 130),
        'B': (2,45)
    }
    basket = skus.split(",")
    if not all(item in prices for item in basket):
        return -1
    
    item_counts = {}
    for item in basket:
        item_counts[item] = item_count



