# noinspection PyUnusedLocal
# skus = unicode string

from collections import Counter
def checkout(skus):
    prices = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15,
        'E': 40,
        'F': 10,
        'G': 20,
        'H': 10,
        'I': 35,
        'J': 60,
        'K': 70,
        'L': 90,
        'M': 15,
        'N': 40,
        'O': 10,
        'P': 50,
        'Q': 30,
        'R': 50,
        'S': 20,
        'T': 20,
        'U': 40,
        'V': 50,
        'W': 20,
        'X': 17,
        "Y": 20,
        "Z": 21
    }

    if not skus:
        return 0
    
    item_counts = Counter(skus)

    if not all(item in prices for item in item_counts):
        return -1
    
    total = 0

    group_discount_items = ['S','T', 'X', 'Y','Z']

    group_items = []

    for item in group_discount_items:
        count = item_counts.get(item,0)
        group_items.extend([item] * count)
        item_counts[item] = 0

    group_items.sort(key=lambda x: prices[x], reverse=True)

    while len(group_items) >= 3:
        total += 45
        for _ in range(3):
            group_items.pop()

    for item in group_items:
        item_counts[item] = item_counts.get(item,0) + 1

    while item_counts.get("A", 0) >= 5:
        total += 200
        item_counts -= 5

    while item_counts.get('A',0) >= 3:
        total += 130
        item_counts

   
    return total




