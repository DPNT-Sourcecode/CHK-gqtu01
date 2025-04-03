

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

    if not skus:
        return 0
    basket = list(skus)
    if not all(item in prices for item in basket):
        return -1
    
    item_counts = {}
    for item in basket:
        item_counts[item] = item_counts.get(item,0) + 1
    
    total = 0

    for item, count in item_counts.items():
        if item in special_offers:
            offer_quantity, offer_price = special_offers[item]

            offer_count = count // offer_quantity

            remain = count % offer_quantity

            total += (offer_count * offer_price) + (remain * prices[item])
        else:

            total += count * prices[item]
    
    return total
